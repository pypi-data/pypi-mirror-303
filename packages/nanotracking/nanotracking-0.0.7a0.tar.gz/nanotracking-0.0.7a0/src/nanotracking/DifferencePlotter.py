#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:52:38 2023

@author: henryingels
"""

import os
import pandas as pd
import numpy as np
import scipy
from scipy.signal import argrelextrema
from collections import OrderedDict
from collections.abc import Iterable
from dataclasses import dataclass
import typing
import traceback
import matplotlib as mpl
resolution = 200
mpl.rcParams['figure.dpi'] = resolution
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.left'] = False
mpl.rcParams['axes.spines.right'] = False
from matplotlib import pyplot as plt, cm
from .sample_class import Sample
from .settings_classes import Calculation, Setting, Settings
from .InfoComparison import compare_info
from .DrawTable import Table
# from nanotracking import data_handler

volume = 2.3E-06
prefix = 'ConstantBinsTable_'
prefix2 = 'Videos_'
suffix = '.dat'
                    
@dataclass
class NeedRefresh:
    settings: set
    data: bool
    tabulation: bool
    peaks: bool
    cumulative: bool
    difference: bool

class NTA():
    def __init__(self, output_folder, truncation_size, xlabel = "Diameter (nm)", ylabel = None, notes_position = -0.15, grid_proportion_of_figure = 0.9, notes_separation = 0.1, normalize = False):
        if ylabel is None:
            if normalize:
                ylabel = "Probability density ($nm^{-1}$)"
            else:
                ylabel = "Particle size distribution (counts/mL/nm)"

        self.output_folder, self.filenames = output_folder, []
        self.table, self.peak_settings = None, None
        self.table_enabled, self.cumulative_enabled, self.difference_enabled = False, False, False
        self.unordered_samples, self.samples, self.samples_setting = dict(), [], Setting('sample', datatype = Sample)
        self.size_binwidth = None

        os.makedirs(output_folder, exist_ok = True)
        self.truncation_size = truncation_size
        self.truncation_index = -1

        self.xlabel, self.ylabel = xlabel, ylabel
        self.fig, self.colors = plt.figure(), cm.plasma(np.linspace(0, 1, 0))
        self.axs = dict()
        # self.cell_height, self.cell_height_transData = None, None
        self.cell_height = None
        self.grid_proportion_of_figure = grid_proportion_of_figure
        self.notes_position, self.notes_separation, self.notes = notes_position, notes_separation, {'difference': None, 'cumulative': None, 'peaks': None}
        
        self.counts_min, self.counts_max = None, None
        self.maxima, self.rejected_maxima = None, None

        self.tmp_filenames = {
            'sizes': os.path.join(output_folder, 'sizes'),
            'counts': os.path.join(output_folder, 'counts'),
            'filtered_counts': os.path.join(output_folder, 'filtered_counts'),
            'top_nm': os.path.join(output_folder, 'top_nm'),
            'fulldata_count_sums': os.path.join(output_folder, 'fulldata_count_sums'),
            'cumulative_sums': os.path.join(output_folder, 'cumulative_sums'),
            'cumsum_maxima': os.path.join(output_folder, 'cumsum_maxima'),
            'count_differences': os.path.join(output_folder, 'count_differences')
        }
        self.calculations = dict()
        self.need_recompute = True
        self.need_refresh = NeedRefresh(settings = set(), data = True, tabulation = True, peaks = False, cumulative = False, difference = False)

        self.normalize = normalize
        
        self.settings = None
        self.configure_settings()
    def load(self, datafolder, filenames):
        def generate_samples():
            for folder in os.listdir(datafolder):
                folder_path = os.path.join(datafolder, folder)
                if os.path.isfile(folder_path): continue
                sample = Sample(folder_path, prefix, suffix, videos_file_prefix = prefix2)
                if sample.filename not in filenames: continue
                yield sample.filename, sample
        unordered_samples = dict(generate_samples()); self.unordered_samples = unordered_samples
        samples, samples_setting = self.samples, self.samples_setting
        for i, name in enumerate(filenames):
            sample = unordered_samples[name]
            sample.index = i
            samples.append(sample)
            samples_setting.set_value(sample, sample)
        num_of_plots = len(samples)
        width, height = mpl.rcParamsDefault["figure.figsize"] # In inches
        height *= (num_of_plots/3)
        height = min(np.floor(65536/resolution), height)
        self.fig.set_size_inches(width, height)
        self.colors = cm.plasma(np.linspace(0, 1, num_of_plots))
        self.truncation_index = self.find_truncation_index(self.truncation_size, samples)
    def find_truncation_index(self, truncation_size, samples):
        '''
        Given a maximum particle size (truncation_size), finds the lowest index of the array returned by NTA.data_of_sample(sample, truncated = False) such that all sizes are below truncation_size.
        This index doesn't apply to NTA.sizes(), NTA.counts(), etc.!
        '''
        truncation_index = -1
        for sample in samples:
            sample_data = self.data_of_sample(sample, truncated = False)
            _truncation_index = np.argmax(sample_data['UpperBinDiameter_[nm]'] > truncation_size)
            truncation_index = max(truncation_index, _truncation_index)
        return truncation_index
    def add_table(self, width, margin_minimum_right, margin_left):
        assert self.table is None, "Table already exists; must first call NTA.delete_table()."
        table = Table(self, width, margin_minimum_right, margin_left)
        self.table = table
        self.need_recompute, self.need_refresh.tabulation = True, True
        return table
    def delete_table(self):
        self.table = None
    def enable_table(self):
        self.table_enabled = True
    def disable_table(self):
        self.table_enabled = False
    def get_setting_or_calculation(self, tag):
        output = self.settings.by_tag(tag)
        if output is None: output = self.calculations[tag]
        assert output is not None, f'Could not find tag "{tag}" in settings or calculations.'
        return output

    def new_calculation(self, name, value_function, *output_names):
        calculation = Calculation(name, value_function, self.output_folder, name, *output_names, samples = self.samples)
        self.calculations[name] = calculation
        need_refresh = self.need_refresh
        need_refresh.tabulation = True
        return calculation
                
    def enable_peak_detection(
            self, gaussian_width, moving_avg_width, gaussian_std_in_bins, second_derivative_threshold, maxima_marker, rejected_maxima_marker,
            filter_description = r"Black lines indicate Gaussian smoothing (a low-pass filter) with $\sigma = {gaussian_std_in_bins}$ bins and convolution kernel of width {gaussian_width} bins.",
            maxima_candidate_description = ": Candidate peaks after smoothing, selected using argrelextrema in SciPy {scipy_version}.",
            maxima_description = ": Peaks with under {second_derivative_threshold} counts/mL/nm$^3$ second derivative, computed after smoothing again with simple moving average of width {moving_avg_width} bins."):
        x = np.linspace(0, gaussian_width, gaussian_width)
        gaussian = np.exp(-np.power((x - gaussian_width/2)/gaussian_std_in_bins, 2)/2)/(gaussian_std_in_bins * np.sqrt(2*np.pi))
        
        peak_settings = locals(); peak_settings.pop('self')
        peak_settings['lowpass_filter'] = gaussian / gaussian.sum()
        peak_settings['filter_description'] = filter_description.format(gaussian_std_in_bins = gaussian_std_in_bins, gaussian_width = gaussian_width)
        peak_settings['maxima_candidate_description'] = maxima_candidate_description.format(scipy_version = scipy.__version__)
        peak_settings['maxima_description'] = maxima_description.format(second_derivative_threshold = second_derivative_threshold, moving_avg_width = moving_avg_width)
        self.peak_settings = peak_settings
        
        self.need_recompute, self.need_refresh.tabulation, self.need_refresh.peaks = True, True, True
    def disable_peak_detection(self):
        self.peak_settings = None
    def enable_cumulative(self):
        self.cumulative_enabled = True
        self.need_recompute, self.need_refresh.tabulation, self.need_refresh.cumulative = True, True, True
    def disable_cumulative(self):
        self.cumulative_enabled = False
    def enable_difference(self, note = "Shadows show difference between a plot and the one above it."):
        self.difference_enabled = True
        self.notes['difference'] = note
        self.need_recompute, self.need_refresh.tabulation, self.need_refresh.difference = True, True, True
    def disable_difference(self):
        self.difference_enabled = False
    def configure_settings(self):
        previous_setting = Setting('previous', name = 'Previous')
        md_settings = [
            Setting('experimental_unit', name = 'Experimental unit'),
            Setting('treatment', name = 'Treatment', units = 'µM'),
            Setting('wait', name = 'Wait', units = 'h'),
            Setting('filter', name = 'Filter cut-on', units = 'nm'),
            previous_setting ]
        red_enabled = Setting('RedLaserEnabled', name = 'Red enabled', datatype = bool)
        green_enabled = Setting('GreenLaserEnabled', name = 'Green enabled', datatype = bool)
        blue_enabled = Setting('BlueLaserEnabled', name = 'Blue enabled', datatype = bool)
        detection_threshold_setting = Setting('DetectionThresholdType', name = 'Detection mode', dependencies_require = 'Manual')
        xml_settings = [
            Setting('RedLaserPower', short_name = '635nm', name = '635nm power', units = 'mW', datatype = int, show_name = True, depends_on = red_enabled),
            red_enabled,
            Setting('GreenLaserPower', short_name = '520nm', name = '520nm power', units = 'mW', datatype = int, show_name = True, depends_on = green_enabled),
            green_enabled,
            Setting('BlueLaserPower', short_name = '445nm', name = '445nm power', units = 'mW', datatype = int, show_name = True, depends_on = blue_enabled),
            blue_enabled,
            Setting('Exposure', units = 'ms', datatype = int),
            Setting('Gain', units = 'dB', datatype = int),
            Setting('MeasurementStartDateTime'),
            Setting('FrameRate', name = 'Framerate', units = 'fps', datatype = int),
            Setting('FramesPerVideo', name = 'Frames per video', units = 'frames', datatype = int),
            Setting('NumOfVideos', name = 'Number of videos', datatype = int),
            Setting('StirrerSpeed', name = 'Stirring speed', units = 'rpm', datatype = int),
            Setting('StirredTime', name = 'Stirred time', units = 's', datatype = int),
            detection_threshold_setting,
            Setting('DetectionThreshold', name = 'Detection threshold', datatype = float, depends_on = detection_threshold_setting) ]
        settings_list = [self.samples_setting, *md_settings, *xml_settings]
        settings = Settings(OrderedDict({setting.tag: setting for setting in settings_list}))
        self.settings = settings

    def data_of_sample(self, sample, truncated = True, truncation_size = None):
        """
        Get the size distribution of a sample, using either its name (a string) or the Sample object itself.
        Returns a Pandas DataFrame.
        If truncated is True, only data with sizes below truncation_size will be returned.
        If truncation_size is None, NTA.truncation_size will be used.
        """
        if type(sample) is not Sample:
            assert type(sample) is str, "Argument of data_of_sample must be of type Sample or string."
            sample = self.unordered_samples[sample]
        all_data = pd.read_csv(sample.dat, sep = '\t ', engine = 'python')
        if truncated:
            if truncation_size is None:
                truncation_index = self.truncation_index
            else:
                truncation_index = self.find_truncation_index(truncation_size, self.samples)
            return all_data.iloc[:truncation_index, :]
        return all_data
    def compute(self, prep_tabulation = True):
        def vstack(arrays):
            if len(arrays) == 0:
                try: return arrays[0]
                except: return arrays # In case "arrays" is an empty list.
            return np.vstack(arrays)
        
        peak_settings = self.peak_settings
        peaks_enabled = (peak_settings is not None)
        need_refresh = self.need_refresh
        refresh_data = need_refresh.data
        refresh_peaks, refresh_cumulative, refresh_difference = (peaks_enabled and need_refresh.peaks), (self.cumulative_enabled and need_refresh.cumulative), (self.difference_enabled and need_refresh.difference)
        if refresh_data:
            all_sizes, all_counts = [], []
        else:
            all_sizes, all_counts = self.sizes(), self.counts()
            size_binwidth = self.size_binwidth
        if refresh_peaks:
            lowpass_filter, moving_avg_width, second_derivative_threshold = peak_settings['lowpass_filter'], peak_settings['moving_avg_width'], peak_settings['second_derivative_threshold']
            all_filtered, all_maxima, all_rejected  = [], [], []
        if refresh_cumulative:
            cumulative_sums, cumsum_maxima = [], []
        if refresh_difference:
            all_count_differences = []
        
        previous_sizes = None
        sizes_min, sizes_max = 0, 0
        counts_min, counts_max = 0, 0
        samples, data_of_sample = self.samples, self.data_of_sample
        for i, sample in enumerate(samples):
            if not refresh_data:
                sizes, counts = all_sizes[i], all_counts[i]
            else:
                data = data_of_sample(sample, truncated = True)
                sizes, counts = data['/LowerBinDiameter_[nm]'].to_numpy(), data['PSD_corrected_[counts/mL/nm]'].to_numpy()
                size_binwidth = sizes[1] - sizes[0]
                
                if previous_sizes is not None:
                    assert np.all(sizes == previous_sizes) == True, 'Unequal sequence of size bins between samples detected!'
                previous_sizes = sizes
                # data_handler.parse_data(sizes.to_numpy(dtype = np.double), counts.to_numpy(dtype = np.double), sample.filename, self.output_folder, num_data_points)
                # data_handler.parse_data(
                #     sizes = sizes.to_numpy(dtype = np.double),
                #     counts = counts.to_numpy(dtype = np.double),
                #     sample_filename = sample.filename,
                #     outputs_path = self.output_folder,
                #     num_data_points = num_data_points)
                all_sizes.append(sizes)
                all_counts.append(counts)

            if refresh_peaks:
                assert len(lowpass_filter) <= len(counts), f"gaussian_width={len(lowpass_filter)} is too big, given {len(counts)=}."
                assert moving_avg_width <= len(counts), f"{moving_avg_width=} is too big, given {len(counts)=}."
                bin_centers = sizes + size_binwidth/2
                filtered = np.convolve(counts, lowpass_filter, mode = 'same')
                maxima_candidates, = argrelextrema(filtered, np.greater)
                twice_filtered = np.convolve(filtered, [1/moving_avg_width]*moving_avg_width, mode = 'same')
                derivative = np.gradient(twice_filtered, bin_centers)
                second_derivative = np.gradient(derivative, bin_centers)
                second_deriv_negative, = np.where(second_derivative < second_derivative_threshold)
                maxima = np.array([index for index in maxima_candidates if index in second_deriv_negative])
                assert len(maxima) != 0, 'No peaks found. The second derivative threshold may be too high.'
                rejected_candidates = np.array([entry for entry in maxima_candidates if entry not in maxima])
                all_filtered.append(filtered); all_maxima.append(maxima); all_rejected.append(rejected_candidates)
            if refresh_cumulative:
                cumulative_sum = np.cumsum(counts)*size_binwidth
                cumulative_sums.append(cumulative_sum); cumsum_maxima.append(cumulative_sum.max())
            if refresh_difference:
                count_differences = []
                for j, other_sample in enumerate(samples):
                    if i == j:
                        count_differences.append(0*counts)
                        continue
                    count_difference = counts - self.counts(sample = other_sample)
                    counts_max = max(count_difference.max(), counts_max)
                    counts_min = min(count_difference.min(), counts_min)
                    count_differences.append(count_difference)
                all_count_differences.append(np.array(count_differences))
            if refresh_data or refresh_difference:
                sizes_max = max((sizes+size_binwidth)[-1], sizes_max)
                sizes_min = min(sizes[0], sizes_min)
                counts_max = max(counts.max(), counts_max)
                counts_min = min(counts.min(), counts_min)
            for setting in tuple(need_refresh.settings):
                value = setting.value_function(sample)
                setting.set_value(sample, value)
                need_refresh.settings.remove(setting)
            previous_counts = counts
        
        tmp_filenames = self.tmp_filenames
        if refresh_data:
            np.save(tmp_filenames['sizes'], vstack(all_sizes))
            np.save(tmp_filenames['counts'], vstack(all_counts))
            self.sizes_min, self.sizes_max = sizes_min, sizes_max
            self.counts_min, self.counts_max = counts_min, counts_max
            self.size_binwidth = previous_sizes[1] - previous_sizes[0]
            need_refresh.data = False
        # np.save(tmp_filenames['total_stds'], vstack(total_stds))
        # np.save(tmp_filenames['avg_histograms'], vstack(avg_histograms))
        if refresh_peaks:
            np.save(tmp_filenames['filtered_counts'], vstack(all_filtered))
            self.maxima, self.rejected_maxima = all_maxima, all_rejected
            need_refresh.peaks = False
        if refresh_cumulative:
            np.save(tmp_filenames['cumulative_sums'], vstack(cumulative_sums))
            np.save(tmp_filenames['cumsum_maxima'], cumsum_maxima)
            need_refresh.cumulative = False
        if refresh_difference:
            np.save(tmp_filenames['count_differences'], np.array(all_count_differences))
            need_refresh.difference = False
        self.need_recompute = False
        if prep_tabulation:
            self.prepare_tabulation()
    def prepare_tabulation(self):
        table, table_enabled, settings, samples = self.table, self.table_enabled, self.settings, self.samples
        num_of_plots = len(samples)
        if table_enabled:
            self.table.reset_columns() # If prepare_tabulation() has been run before, remove the columns for treatments and waits.
            column_names, column_widths = table.column_names, table.column_widths
            include_experimental_unit, treatments_and_waits = table.include_experimental_unit, table.treatments_and_waits
            include_treatments = (treatments_and_waits is not None)
            if include_treatments:
                treatments_waits_columnIndex = treatments_and_waits[0]
            else:
                treatments_waits_columnIndex = -1
        
        def generate_rows():
            column_quantities = dict()
            def number_of_subtags(tag):
                if (setting := settings.by_tag(tag)) is None: return 0
                return max(len(setting.subsettings), 1)
            def get_multivalued(tag, sample):
                if (setting := settings.by_tag(tag)) is None: return []
                if len(setting.subsettings) == 0:
                    value = setting.get_value(sample)
                    if value is None: return []
                    return [value]
                subsettings = list(setting.numbered_subsettings.items())
                subsettings.sort()
                values = [subsetting.get_value(sample) for _, subsetting in subsettings]
                if values[0] is None:
                    values[0] = setting.get_value(sample)
                return values
            for i in range(num_of_plots):
                sample = samples[i]
                settings.read_files(sample)
                settings.parse_time(sample)
                if table_enabled and include_treatments:
                    for tag in ('treatment', 'wait'):
                        quantity = number_of_subtags(tag)
                        if tag not in column_quantities:
                            column_quantities[tag] = quantity
                            continue
                        column_quantities[tag] = max(column_quantities[tag], quantity)
            
            if not table_enabled: return
            
            if include_treatments:
                num_of_treatments, num_of_waits = column_quantities['treatment'], column_quantities['wait']
                treatment_column_name, treatment_column_width = treatments_and_waits[1]
                wait_column_name, wait_column_width = treatments_and_waits[2]
                index = 0
                for i in range(max(num_of_treatments, num_of_waits)):
                    if i < num_of_treatments:
                        column_names.insert(treatments_waits_columnIndex + index, treatment_column_name.format(treatment_number = i + 1))
                        column_widths.insert(treatments_waits_columnIndex + index, treatment_column_width)
                        index += 1
                    if i < num_of_waits:
                        column_names.insert(treatments_waits_columnIndex + index, wait_column_name.format(wait_number = i + 1))
                        column_widths.insert(treatments_waits_columnIndex + index, wait_column_width)
                        index += 1
            
            for i in range(num_of_plots):
                row = []
                sample = samples[i]

                if include_treatments:
                    treatments = get_multivalued('treatment', sample)
                    waits = get_multivalued('wait', sample)
                    for j in range( max(column_quantities['treatment'], column_quantities['wait']) ):
                        if j < len(treatments): row.append(treatments[j])
                        elif j < column_quantities['treatment']: row.append(None)
                        if j < len(waits): row.append(waits[j])
                        elif j < column_quantities['wait']: row.append(None)
                if include_experimental_unit:
                    experimental_unit = settings.by_tag('experimental_unit')
                    text = ''
                    if experimental_unit is not None:
                        value = experimental_unit.get_value(sample)
                        text += value if value is not None else ''
                        if hasattr(experimental_unit, 'age'):
                            age = experimental_unit.age.get_value(sample)
                            text += f"\n{age:.1f} d old" if age is not None else ''
                    row.append(text)
                columns = list(table.columns_as_Settings_object.column_numbers.items())
                columns.sort()
                for j, column in columns:
                    # content = '\n'.join(
                    #     setting.show_name*f"{setting.short_name}: " + f"{setting.get_value(sample)}" + setting.show_unit*f" ({setting.units})"
                    #     for setting in column if setting.get_value(sample) is not None )
                    # row.append(content)
                    assert len(column) == 1, "There can be only one Setting object per column."
                    if column[0].tag.startswith('COLUMN'):
                        group = column[0]
                        grouped_settings = group.subsettings.values()
                        row.append(group.format(*(setting.get_value(sample) for setting in grouped_settings)))
                    elif column[0].tag.startswith('CALC'):
                        group = column[0]
                        grouped_settings = group.subsettings.values()
                        row.append(group.format(*(subsetting.get_value(sample) for subsetting in grouped_settings)))
                    else:
                        setting = column[0]
                        row.append(setting.format(setting.get_value(sample)))
                
                row.append("")
                yield row
        self.rows = tuple(generate_rows())
        self.need_refresh.tabulation = False
    def compare(self):
        assert self.need_recompute == False, "Must run NTA.compute() first."
        assert self.need_refresh.tabulation == False, "Must run NTA.prepare_tabulation() first."
        compare_info(self.settings, self.samples, self.calculations, self.output_folder)
    def load_tempfile(self, key):
        filename = self.tmp_filenames[key]+'.npy'
        try:
            data = np.load(filename)
        except OSError:
            raise Exception(f"Couldn't find {filename}.")
        return data
    def sizes(self, sample = None, size_range = None, lower = True, middle = False, upper = False):
        '''
        Get a 1D array of particle sizes from one or more samples. Use NTA.counts() to get the corresponding 1D array of particle counts.

        Parameters
        ----------
            sample: Sample
                The sample to use. If not specified, all samples will be used.
            size_range: iterable
                The size range of the particles to return, specified as an iterable of the form (a, b); "a" is the lowest size, while "b" is the highest. If not specified, all particle sizes will be returned.
        '''
        assert (lower + middle + upper) == 1, "Must set either lower, middle, or upper to True, but not more than one."
        
        if size_range is not None:
            assert isinstance(size_range, Iterable), f"Argument size_range must be iterable; got type {type(size_range)}."
            assert len(size_range) == 2, f"Argument size_range must have length 2; got length {len(size_range)}."
            assert sample is not None, "Must specify a sample when using size_range."
            middle_bins = self.sizes(sample = sample, size_range = None, lower = False, upper = False, middle = True)
            half_size_binwidth = self.size_binwidth / 2
            left_bound, right_bound = size_range
            in_bounds, = np.where(((middle_bins - half_size_binwidth) >= left_bound) & ((middle_bins + half_size_binwidth) <= right_bound))
        
        all_sizes = self.load_tempfile('sizes') # Load lower (leftmost) side of each size bin
        all_sizes += (0.5*middle + 1*upper) * self.size_binwidth
        if sample is not None:
            assert sample.index is not None, f"The provided Sample object \"{sample.filename}\" has no index."
            sample_sizes = all_sizes[sample.index]
            if size_range is not None:
                return sample_sizes[in_bounds]
            return sample_sizes
        return all_sizes
    def counts(self, sample = None, size_range = None):
        '''
        Get a 1D array of particle counts from one or more samples. Use NTA.sizes() to get the corresponding 1D array of particle sizes.

        Parameters
        ----------
            sample: Sample
                The sample to use. If not specified, all samples will be used.
            size_range: iterable
                The size range of the particles being counted, specified as an iterable of the form (a, b); "a" is the lowest size, while "b" is the highest. If not specified, all particles will be counted.
        '''
        if size_range is not None:
            assert isinstance(size_range, Iterable), f"Argument size_range must be iterable; got type {type(size_range)}."
            assert len(size_range) == 2, f"Argument size_range must have length 2; got length {len(size_range)}."
            assert sample is not None, "Must specify a sample when using size_range."
            middle_bins = self.sizes(sample = sample, size_range = None, lower = False, upper = False, middle = True)
            half_size_binwidth = self.size_binwidth / 2
            left_bound, right_bound = size_range
            in_bounds, = np.where(((middle_bins - half_size_binwidth) >= left_bound) & ((middle_bins + half_size_binwidth) <= right_bound))
        
        all_counts = self.load_tempfile('counts')
        if sample is not None:
            assert sample.index is not None, f"The provided Sample object \"{sample.filename}\" has no index."
            sample_counts = all_counts[sample.index]
            if size_range is not None:
                return sample_counts[in_bounds]
            return sample_counts
        return all_counts
    # def cell_to_data_coordinates(self, cell_coords):
    #     '''
    #     Convert "cell coordinates" (y=0 at one sample's x-axis, y=1 at that of the sample above) to data coordinates.
    #     The x coordinate is taken to remain unchanged between cell and data coordinates.
    #     '''
    #     assert isinstance(cell_coords, Iterable), f"Argument cell_coords must be iterable with length 2; got type {type(cell_coords)}."
    #     assert len(cell_coords) == 2, f"Argument cell_coords must have length 2; got length {len(cell_coords)}."
    #     cell_x, cell_y = cell_coords
    #     return cell_x, cell_y*self.cell_height_transData
    def data_to_figure_coords(self, ax, data_x, data_y):
        transFigure = ax.figure.transFigure
        points = np.array([data_x, data_y], dtype = np.float64).T
        points_transDisplay = ax.transData.transform(points)
        points_transFigure = transFigure.inverted().transform(points_transDisplay)
        x, y = points_transFigure.T
        return x, y
    def ax_origin_figure_coords(self, ax):
        (origin_x,), (origin_y,) = self.data_to_figure_coords(ax, [0], [0])
        return origin_x, origin_y
    def plot(self, *samples, grid_color = '0.8', name = 'Ridgeline plot'):
        assert self.need_recompute == False, "Must run NTA.compute() first."
        if len(samples) != 0:
            samples = [self.unordered_samples[key] for key in samples]
        else:
            samples = self.samples
        num_of_plots = len(samples)
        colors, table, peak_settings, output_folder = self.colors, self.table, self.peak_settings, self.output_folder
        sizes_min, sizes_max, counts_min, counts_max = self.sizes_min, self.sizes_max, self.counts_min, self.counts_max
        peaks_enabled = (peak_settings is not None)
        table_enabled = self.table_enabled
        cumulative_enabled, difference_enabled = self.cumulative_enabled, self.difference_enabled
        if table_enabled:
            assert self.need_refresh.tabulation == False, "Must run NTA.prepare_tabulation() first."
        all_sizes, all_counts = self.sizes(), self.counts()
        tmp_filenames = self.tmp_filenames
        if peaks_enabled:
            rejected_maxima_marker, maxima_marker, filter_description, maxima_candidate_description, maxima_description = peak_settings['rejected_maxima_marker'], peak_settings['maxima_marker'], peak_settings['filter_description'], peak_settings['maxima_candidate_description'], peak_settings['maxima_description']
            all_filtered = np.load(tmp_filenames['filtered_counts']+'.npy')
            all_maxima, all_rejected = self.maxima, self.rejected_maxima
        if cumulative_enabled:
            cumulative_sums = np.load(tmp_filenames['cumulative_sums']+'.npy')
            cumsum_maxima = np.load(tmp_filenames['cumsum_maxima']+'.npy')
            max_of_cumulative_sums = cumsum_maxima.max()
            cumulative_sum_scaling = counts_max / max_of_cumulative_sums
        if difference_enabled:
            all_count_differences = np.load(tmp_filenames['count_differences']+'.npy')

        fig = self.fig; plt.figure(fig)
        fig.clear()
        axs = fig.subplots(num_of_plots, 1, squeeze = False)
        axs = axs[:,0]  # Flatten axs from a 2D array (of size num_of_plots x 1) to a 1D array
        self.axs = {samples[i]: ax for i, ax in enumerate(axs)}
        (_, height) = fig.get_size_inches()
        fig.subplots_adjust(hspace=-0.05*height)
        transFigure = fig.transFigure
        transFigure_inverted = transFigure.inverted()

        final_i = num_of_plots - 1


        previous_sample = None
        for i, ax in enumerate(axs):
            sample = samples[i]
            sample_index = sample.index
            try:
                sizes, counts = all_sizes[sample_index], all_counts[sample_index]
            except IndexError as ie:
                raise IndexError(f"Iterables `all_sizes` and `all_counts` have lengths {len(all_sizes)} and {len(all_counts)}; got index {sample_index}.") from ie
            # sizes, counts = data_handler.read_data(sample_filename = sample.filename, outputs_path = output_folder, num_data_points = num_data_points)
            size_binwidth = sizes[1] - sizes[0]
            bin_centers = sizes + size_binwidth/2
            # avg_histogram, total_std = avg_histograms[sample_index], total_stds[sample_index]
            
            plt.sca(ax)
            total_conc = np.sum(counts*size_binwidth)
            counts_scale = total_conc if self.normalize else 1
            plt.bar(sizes, counts/counts_scale, width = size_binwidth, color = colors[sample_index], alpha = 0.7, align = 'edge')
            
            if peaks_enabled:
                filtered, maxima, rejected_candidates = all_filtered[sample_index], all_maxima[sample_index], all_rejected[sample_index]
                plt.plot(sizes, filtered/counts_scale, linewidth = 0.5, color = 'black')
                if len(rejected_candidates) != 0:
                    plt.plot(bin_centers[rejected_candidates], filtered[rejected_candidates]/counts_scale, **rejected_maxima_marker)
                plt.plot(bin_centers[maxima], filtered[maxima]/counts_scale, **maxima_marker)
            
            if difference_enabled and i != 0:
                assert previous_sample is not None
                count_differences = all_count_differences[sample_index][previous_sample.index]
                plt.bar(sizes, count_differences/counts_scale, width = size_binwidth, color = 'black', alpha = 0.3, align = 'edge')
            
            videos = sample.videos
            all_histograms = np.array([np.histogram(video, bins = sizes)[0] for video in videos])
            avg_histogram = np.average(all_histograms, axis = 0)
            total_std = np.std(all_histograms, axis = 0, ddof = 1)
            scale_factor = np.array([counts[j]/avg if (avg := avg_histogram[j]) != 0 else 0 for j in range(len(counts)-1)])
            avg_histogram *= scale_factor
            error_resizing = 0.1
            total_std *= scale_factor * error_resizing
            errorbars = np.array(list(zip(total_std, [0]*len(total_std)))).T
            plt.errorbar(bin_centers[:-1], avg_histogram/counts_scale, yerr = errorbars/counts_scale, elinewidth = 1, linestyle = '', marker = '.', ms = 1, alpha = 0.5, color = 'black')            
            
            plt.xlim(sizes_min, sizes_max)
            plt.ylim(counts_min/counts_scale, counts_max/counts_scale)
            ax.patch.set_alpha(0)
                
            if i == final_i:
                ax.yaxis.get_offset_text().set_x(-0.1)
                plt.xlabel(self.xlabel)
                plt.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0, 0))
                ax.spines.left.set_visible(True)
                plt.axhline(0, color = 'black', linewidth = 1) # Accounts for case when the final (bottom) plot contains negative data/calculations, meaning there should be a "fake" x-axis at y=0. (The real one has tick marks.)
            else:
                plt.yticks([]); plt.xticks([])
                ax.spines['bottom'].set_position(('data', 0))

            
            if cumulative_enabled:
                cumulative_sum = cumulative_sums[sample_index]
                if self.normalize:
                    origin_x, origin_y = self.ax_origin_figure_coords(ax)
                    sizes_transFigure, _ = self.data_to_figure_coords(ax, sizes, sizes)
                    scaled_cumulative = self.cell_height * (cumulative_sum/cumulative_sum[-1])
                    plt.plot(sizes_transFigure, scaled_cumulative + origin_y, transform = transFigure, color = 'red', linewidth = 0.5)
                else:
                    plt.plot(sizes, cumulative_sum*cumulative_sum_scaling/counts_scale, color = 'red', linewidth = 0.5)

            previous_sample = sample

        if len(axs) != 1:
            assert len(axs) != 0, "No Axes objects present!"
            origin0, origin1, origin_last = self.ax_origin_figure_coords(axs[0]), self.ax_origin_figure_coords(axs[1]), self.ax_origin_figure_coords(axs[-1])
            (x0, y0), (x1, y1), (x_last, y_last) = origin0, origin1, origin_last
            cell_height = y0 - y1
            table_top = y0 + 0.5*cell_height
            table_bottom = y_last - 0.5*cell_height
            self.cell_height = cell_height
        else:
            y0 = cell_height = table_top = 1
            y1 = table_bottom = 0 
            self.cell_height = cell_height
        _, y0_transDisplay = transFigure.transform([0, y0])
        _, y1_transDisplay = transFigure.transform([0, y1])
        _, y0_transData = axs[0].transData.inverted().transform([0, y0_transDisplay])
        _, y1_transData = axs[0].transData.inverted().transform([0, y1_transDisplay])
        # self.cell_height_transData = y0_transData - y1_transData

        for i, ax in enumerate(axs):
            sample = samples[i]
            for calculation in tuple(self.calculations.values()):
                visuals = calculation.visuals
                if len(visuals) == 0: continue
                for visual_name, visual in visuals.items(): # TODO: add specific visuals before running NTA.plot() instead of plotting all of them
                    calculation.apply_visual(visual_name, sample, ax)

        final_ax = axs[-1]
        plt.sca(final_ax)
        final_ax.xaxis.set_tick_params(width = 2); final_ax.yaxis.set_tick_params(width = 2)
        transData = final_ax.transData

        tick_values, tick_labels = plt.xticks()
        final_i = len(tick_values) - 1
        right_edge_figure = None
        grid_proportion_of_figure = self.grid_proportion_of_figure
        for i, tick_value in enumerate(tick_values):
            display_coords = transData.transform([tick_value, counts_min])
            figure_x, figure_y = transFigure_inverted.transform(display_coords)
            
            line = plt.Line2D([figure_x, figure_x], [figure_y, grid_proportion_of_figure], lw = 1, color = grid_color, transform = transFigure, zorder = 0)
            fig.add_artist(line)
            line.set_clip_on(False)
            
            if i == final_i:
                right_edge_figure = figure_x

        plt.text(0, 0.45, self.ylabel, fontsize=12, transform = transFigure, rotation = 'vertical', verticalalignment = 'center')
        text_y = 0 + self.notes_position
        if difference_enabled:
            plt.text(0, text_y, self.notes['difference'], fontsize=12, transform = transFigure, verticalalignment = 'center')
        if peaks_enabled:
            text_y -= self.notes_separation
            plt.text(0, text_y, filter_description, fontsize=12, transform = transFigure, verticalalignment = 'center')
        if cumulative_enabled:
            text_y -= self.notes_separation
            if self.normalize:
                plt.text(0, text_y, f"Red lines are integrals of the probability density, ranging from 0 to 1 and scaled to fit their plots.", fontsize=12, transform = transFigure, verticalalignment = 'center')
            else:
                plt.text(0, text_y, f"Red lines are integrals of unsmoothed data, scaled by {cumulative_sum_scaling:.3}.", fontsize=12, transform = transFigure, verticalalignment = 'center')
        if peaks_enabled:
            icon_x, text_x = 0.01, 0.02
            text_y -= self.notes_separation
            rejected_maxima_icon, = plt.plot([icon_x], [text_y], **rejected_maxima_marker, transform = transFigure)
            rejected_maxima_icon.set_clip_on(False)
            plt.text(text_x, text_y, maxima_candidate_description, fontsize=12, transform = transFigure, verticalalignment = 'center')
            
            text_y -= self.notes_separation
            maxima_icon, = plt.plot([icon_x], [text_y], **maxima_marker, transform = transFigure)
            maxima_icon.set_clip_on(False)
            plt.text(text_x, text_y, maxima_description, fontsize=12, transform = transFigure, verticalalignment = 'center')
        text_y -= self.notes_separation
        plt.text(0, text_y, "Measured at room temperature.", fontsize=12, transform = transFigure, verticalalignment = 'center')
        text_y -= self.notes_separation
        plt.text(0, text_y, " ", fontsize=12, transform = transFigure, verticalalignment = 'center')

        if table_enabled:
            edges = {'right': right_edge_figure, 'bottom': table_bottom, 'top': table_top}
            table.draw(fig, ax, [self.rows[sample.index] for sample in samples], edges, grid_color)

        fig.savefig(f"{output_folder}/{name}.png", dpi = 300, bbox_inches='tight')
