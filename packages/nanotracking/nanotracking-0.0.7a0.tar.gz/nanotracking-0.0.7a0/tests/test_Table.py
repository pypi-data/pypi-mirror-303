from pathlib import Path
import unittest
from src.nanotracking import DifferencePlotter
from src.nanotracking import settings_classes
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as path_effects

class Test_Table(unittest.TestCase):
    filenames = ["1-1e5 150nm Nanosphere", "1-1e5 150nm Nanosphere 2", "1-1e5 150nm Nanosphere 32ms", "1-1e5 150nm Nanosphere diff detection setting"]
    specifiers = "All measurements"
    samples = filenames
    normalize = False
    def setUp(self):
        filenames = self.filenames
        nta = DifferencePlotter.NTA(
            output_folder = f"tests/Test output/{self.specifiers}/{self.id()}",
            truncation_size = 400, # nanometers
            normalize = self.normalize
        )
        nta.load(
            datafolder = "tests/Test data",
            filenames = filenames
        )
        nta.compute()
        self.num_of_plots = len(filenames)
        self.table_options = {
            'width': 2.7,
            'margin_minimum_right': 0.03,
            'margin_left': 0.2
        }
        self.nta = nta
        self.table = None
    def add_columns(self):
        nta = self.nta
        table = self.table
        table.add_treatments_and_waits("Treatment\n{treatment_number}\n(µM)", 0.2, "4°C\nwait\n{wait_number}\n(h)", 0.07)
        table.add_settings_by_tag('filter', column_name = "Filter\ncut-on\n(nm)", column_width = 0.1)
        table.add_settings_by_tag('RedLaserPower', 'GreenLaserPower', 'BlueLaserPower', column_name = "Power\n(mW)", column_width = 0.19)
        table.add_settings_by_tag('Exposure', 'Gain', column_name = "Exposure\n(ms),\ngain (dB)", column_width = 0.14)
        def get_detection_info(threshold_type, threshold):
            if threshold is None: return threshold_type
            if threshold_type == 'Polydisperse': return threshold_type
            return f"{threshold_type}\n{threshold}"
        table.add_settings_by_tag('DetectionThresholdType', 'DetectionThreshold', column_name = "Detection\nsetting", column_width = 0.19, format = get_detection_info)
        
        def get_video_info(framerate, frames_per_video, num_of_videos):
            video_duration = frames_per_video / framerate
            if video_duration.is_integer():
                video_duration = int(video_duration)
            return f"{video_duration}x{num_of_videos}"
        table.add_settings_by_tag('FrameRate', 'FramesPerVideo', 'NumOfVideos', column_name = "Video sec\nx quantity", column_width = 0.16, format = get_video_info)

        stir_format = '{StirredTime}x{StirrerSpeed}'
        table.add_settings_by_tag('StirredTime', 'StirrerSpeed', column_name = "Stir sec\nx RPM", column_width = 0.12, format = stir_format)
        
        def get_ID_info(ID):
            return '\n'.join((ID[0:4], ID[4:8], ID[8:12]))
        table.add_settings_by_tag('ID', column_name = "ID", column_width = 0.1, format = get_ID_info)
        
        settings = nta.settings
        samples, unordered_samples = nta.samples, nta.unordered_samples
        def get_previous_ID_info(previous):
            if previous is None: return ''
            previous_sample = unordered_samples[previous]
            ID_of_previous = settings.by_tag('ID').get_value(previous_sample)
            return '\n'.join((ID_of_previous[0:4], ID_of_previous[4:8], ID_of_previous[8:12]))
        table.add_settings_by_tag('previous', column_name = "ID of\nprevious", column_width = 0.13, format = get_previous_ID_info)


        data_to_figure_coords = nta.data_to_figure_coords
        ax_origin_figure_coords = nta.ax_origin_figure_coords

        
        def value_function(sample):
            sizes, counts = nta.sizes(sample = sample), nta.counts(sample = sample)
            cumulative = np.cumsum(counts * nta.size_binwidth)
            return sizes, cumulative
        def bulk_value_function(samples, all_sizes, all_cumulative):
            '''
            Runs after values for all samples have been calculated via value_function().
            Calculates additional values that will be used in visual_function().
            '''
            cumsum_maxima = []
            for sample, sizes, cumulative in zip(samples, all_sizes, all_cumulative):
                cumsum_maxima.append(cumulative.max())
            max_of_cumulative_sums = max(cumsum_maxima)
            counts_max = nta.counts_max
            cumulative_sum_scaling = counts_max / max_of_cumulative_sums
            return (cumulative_sum_scaling,)
        def visual_function(ax, sizes, cumulative, cumulative_sum_scaling):
            if self.normalize:
                sizes_transFigure, _ = data_to_figure_coords(ax, sizes, sizes)
                origin_x, origin_y = ax_origin_figure_coords(ax)
                scaled_cumulative = nta.cell_height * (cumulative/cumulative[-1])
                ax.plot(sizes_transFigure, scaled_cumulative + origin_y, '--', transform = ax.figure.transFigure, color = 'blue')
                return
            ax.plot(sizes, cumulative_sum_scaling*cumulative, '--', color = 'blue')
        cumulative_calc = nta.new_calculation('Cumulative', value_function, 'sizes', 'cumulative') 
        cumulative_calc.add_bulk_value(bulk_value_function)
        # cumulative_calc.add_visual('Cumulative_plot', visual_function)
        cumulative_calc.refresh(*samples)

        times = settings.by_tag('time')
        def value_function(sample):
            all_counts = nta.counts(sample = sample)

            lowest_size, highest_size = 0, 200 # nanometers
            size_range = (lowest_size, highest_size)
            counts_in_range = nta.counts(sample = sample, size_range = size_range)
            sizes_in_range = nta.sizes(sample = sample, size_range = size_range, lower = False, upper = True)

            max_size = max(sizes_in_range)
            if max_size.is_integer():
                max_size = int(max_size)
            min_size = min(sizes_in_range)
            if min_size.is_integer():
                min_size = int(min_size)
            size_binwidth = nta.size_binwidth
            total_conc = np.sum(all_counts)*size_binwidth
            assert total_conc == np.sum(all_counts*size_binwidth)
            total_conc_in_range = np.sum(counts_in_range*size_binwidth)
            
            sample_index = sample.index
            time = times.get_value(sample) # times accessed via closure
            time_since_previous = None
            previous = settings.by_tag('previous').get_value(sample)
            if previous is not None:
                if previous not in unordered_samples:
                    time_since_previous = '?'
                else:
                    previous_sample = unordered_samples[previous]
                    time_of_previous = settings.by_tag('time').get_value(previous_sample)
                    time_since_previous = int((time - time_of_previous).total_seconds())
            above = samples[sample_index - 1] if sample_index != 0 else None
            time_since_above = None
            if above is not None:
                time_of_above = times.get_value(above)
                time_since_above = int((time - time_of_above).total_seconds())
            return previous, time_since_previous, time_since_above, total_conc, total_conc_in_range, min_size, max_size
        font_path = Path("src/nanotracking/fonts/JuliaMono-Regular.ttf")
        def visual_function(ax, previous, time_since_previous, time_since_above, total_conc, total_conc_in_range, min_size, max_size):
            plt.sca(ax)
            origin_x, origin_y = ax_origin_figure_coords(ax)
            # bottom, top = nta.cell_to_data_coordinates((0, 1))
            bottom, top = origin_y, origin_y + nta.cell_height
            (x_min, x_max), _ = data_to_figure_coords(ax, ax.get_xlim(), [0, 0])
            rect_width, rect_height = 0.1*(x_max - x_min), 0.25*(top - bottom)
            text_style = {'color': 'black', 'font': font_path, 'fontsize': 'large'}
            text_outline_style = {'linewidth': 2, 'foreground': 'white'}
            
            transFigure = ax.figure.transFigure
            (min_size_transFigure,), _ = data_to_figure_coords(ax, [min_size], [0])
            l, = plt.plot([min_size_transFigure]*2, [bottom, top], transform = transFigure, color = 'lime', linewidth = 1) 
            # l.set_clip_on(False)
            rect = patches.Rectangle((min_size_transFigure, top - rect_height), rect_width, rect_height, transform = transFigure, edgecolor = 'none', facecolor = 'lime', alpha = 0.5)#linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            text = plt.text(min_size_transFigure + 0.2*rect_width, top - 0.7*rect_height, 'Min', transform = transFigure, **text_style)
            text.set_path_effects([
                path_effects.Stroke(**text_outline_style),
                path_effects.Normal() ])

            (max_size_transFigure,), _ = data_to_figure_coords(ax, [max_size], [0])
            l, = plt.plot([max_size_transFigure]*2, [bottom, top], transform = transFigure, color = 'magenta', linewidth = 1) 
            # l.set_clip_on(False)
            rect = patches.Rectangle((max_size_transFigure, top - rect_height), rect_width, rect_height, transform = transFigure, edgecolor = 'none', facecolor = 'magenta', alpha = 0.5)#linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            text = plt.text(max_size_transFigure + 0.2*rect_width, top - 0.7*rect_height, 'Max', transform = transFigure, **text_style)
            text.set_path_effects([
                path_effects.Stroke(**text_outline_style),
                path_effects.Normal() ])
        calculation = nta.new_calculation(
            'Previous-time-concentrations', value_function,
            'previous', 'time_since_previous', 'time_since_above', 'total_conc', 'total_conc_in_range', 'min_size', 'max_size')
        calculation.add_visual('Size_range', visual_function)
        calculation.refresh(*samples)
        def get_time_info(previous, time_since_previous, time_since_above, total_conc, total_conc_in_range, min_size, max_size):
            text = []
            if time_since_above is not None:
                text.append(f"{time_since_above} since above")
            if time_since_previous is not None:
                text.append(f"{time_since_previous} since previous")
            return '\n'.join(text)
        calculation.add_format('Time format', get_time_info)
        def get_conc_info(previous, time_since_previous, time_since_above, total_conc, total_conc_in_range, min_size, max_size):
            return f'Total: {total_conc:.2E}\n{min_size}-{max_size}nm: {total_conc_in_range:.2E}'
        calculation.add_format('Concentration format', get_conc_info)
        table.add_calculation(calculation, 'Time format', column_name = "Time (s)", column_width = 0.33)
        table.add_calculation(calculation, 'Concentration format', column_name = "Concentration\n(counts/mL)", column_width = 0.3)

        def get_sample_name(sample):
            return sample.name
        letters_per_line, no_hyphens = 12, True
        table.add_settings_by_tag('sample', column_name = "Sample name", column_width = 0.25, format = get_sample_name, letters_per_line = letters_per_line, no_hyphens = no_hyphens)
        table.add_settings_by_tag('experimental_unit', column_name = "Experimental\nunit", column_width = 0.25, letters_per_line = letters_per_line, no_hyphens = no_hyphens)
            

    def get_num_columns(self):
        table = self.table
        num_column_names = len(table.column_names_without_treatmentsOrWaits)
        assert len(table.column_widths_without_treatmentsOrWaits) == num_column_names, "Unequal numbers of column widths and names."
        return num_column_names

    def test_number_of_columns(self):
        nta = self.nta
        self.table = nta.add_table(**self.table_options)
        nta.enable_table()
        self.add_columns()
        self.get_num_columns()
    
    def setup_test_persistence(self):
        nta = self.nta
        self.table = nta.add_table(**self.table_options)
        nta.enable_table()
        self.add_columns()
        num_columns = self.get_num_columns()
        nta.compute(prep_tabulation = False)
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.compute().")
        nta.prepare_tabulation()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.prepare_tabulation().")
        self.assertEqual(self.num_of_plots, len(nta.samples), "Number of plots has changed.")
        nta.plot(*self.samples, name = "Initial plot")
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.plot().")
        return num_columns
    def finish_test_persistence(self, num_columns):
        nta = self.nta
        nta.compute(prep_tabulation = False)
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.compute().")
        nta.prepare_tabulation()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.prepare_tabulation().")
        nta.disable_table()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.disable_table().")
        nta.plot(*self.samples, name = "Final plot, no table")
        nta.enable_table()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.enable_table().")
        nta.plot(*self.samples, name = "Final plot, with table")
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.plot().")
        nta.compare()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.compare().")
    def test_persistence_with_peakfinding(self):
        nta = self.nta
        num_columns = self.setup_test_persistence()
        nta.enable_peak_detection(
            gaussian_width = 30,
            gaussian_std_in_bins = 4,
            moving_avg_width = 20,
            second_derivative_threshold = -30,
            maxima_marker = {'marker': 'o', 'fillstyle': 'none', 'color': 'black', 'linestyle': 'none'},
            rejected_maxima_marker = {'marker': 'o', 'fillstyle': 'none', 'color': '0.5', 'linestyle': 'none'}
        )
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.enable_peak_detection().")
        self.finish_test_persistence(num_columns)
    def test_persistence_with_cumulative(self):
        nta = self.nta
        num_columns = self.setup_test_persistence()
        nta.enable_cumulative()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.enable_cumulative().")
        self.finish_test_persistence(num_columns)
    def test_persistence_with_difference(self):
        nta = self.nta
        num_columns = self.setup_test_persistence()
        nta.enable_difference()
        self.assertEqual(num_columns, self.get_num_columns(), "Column count changed after running NTA.enable_difference().")
        self.finish_test_persistence(num_columns)

class Test_Table_OneMeasurement(Test_Table):
    filenames = ["1-1e5 150nm Nanosphere"]
    specifiers = "One measurement"
    samples = filenames
class Test_Table_TwoMeasurements(Test_Table):
    filenames = ["1-1e5 150nm Nanosphere", "1-1e5 150nm Nanosphere 2"]
    specifiers = "Two measurements"
    samples = filenames
class Test_Table_TwoMeasurements_Switched(Test_Table):
    filenames = ["1-1e5 150nm Nanosphere", "1-1e5 150nm Nanosphere 2"]
    specifiers = "Two measurements"
    samples = filenames[::-1]

class Test_Table_Normalized(Test_Table):
    normalize = True
    specifiers = "Normalized"

if __name__ == '__main__':
    unittest.main()
