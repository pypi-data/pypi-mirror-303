import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 

class Object_Detection_Plot:
    def __init__(self, blind_spot_path=None,
                  top_misses_path=None, table_json_path=None,
                    mixed_json_path=None, overall_json_path=None,
                      confidence_histogram_path=None,
                      output_dir=None):
        self.output_dir = output_dir
        if blind_spot_path:
            self.result_dict = self._load_json(blind_spot_path)
        elif top_misses_path:
            self.new_json_data = self._load_json(top_misses_path)        
        elif table_json_path:
            self.table_json_data = self._load_json(table_json_path)
        elif mixed_json_path:
            self.mixed_json_data = self._load_json(mixed_json_path)        
        elif overall_json_path:
            self.overall_json_data = self._load_json(overall_json_path)        
        elif confidence_histogram_path:
            self.confidence_histogram_data = self._load_json(confidence_histogram_path)
    
    def _load_json(self, json_path):
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data
        
    def draw(self, plot_type, blind_spot_args=None,  
              top_misses_args=None, classbased_table_args=None, mixed_args=None,
                overall_args=None, confidence_histogram_args=None,
                save_path=None):
        if plot_type == 'blind_spot':
            self._plot_blind_spot(blind_spot_args, save_path)
        elif plot_type == 'top_misses':
            self._plot_top_misses(top_misses_args, save_path)
        elif plot_type == 'classbased_table':
            self._plot_classbased_table_metrics(classbased_table_args, save_path)
        elif plot_type == 'mixed_plot':
            self._plot_mixed_metrics(mixed_args, save_path)        
        elif plot_type == 'overall_metrics':
            self._plot_overall_metrics(overall_args, save_path)
        elif plot_type == 'confidence_histogram':
           self._plot_confidence_histogram(confidence_histogram_args, save_path)
        else:
            raise ValueError(f"Unsupported plot type: {plot_type}")
    
    def _plot_blind_spot(self, blind_spot_args, save_path):
        if not self.result_dict or 'Average' not in self.result_dict:
            print("No valid 'Average' data found in the JSON.")
            return
        
        data = self.result_dict['Average']
        df = pd.DataFrame([(k, v) for k, v in data.items() if v != "None"], columns=['Metric', 'Value'])
        df['Value'] = df['Value'].astype(float)
        
        if blind_spot_args:
            if 'Average' in blind_spot_args:
                df = df[df['Metric'].isin(blind_spot_args['Average'])]
            if 'threshold' in blind_spot_args:
                df = df[df['Value'] > blind_spot_args['threshold']]
        
        df = df.sort_values('Value', ascending=False)
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Value', y='Metric', hue='Metric', data=df, palette='viridis')
        plt.title('Average Metrics', fontsize=16)
        plt.xlabel('Value', fontsize=12)
        plt.ylabel('Metric', fontsize=12)
        for i, v in enumerate(df['Value']):
            plt.text(v, i, f' {v:.4f}', va='center')
        if save_path:
            plt.savefig(save_path)
        else:
            plt.savefig('average_metrics.png')
        plt.show()
        plt.close()
        
    def _plot_overall_metrics(self, overall_args, save_path):
        if not self.overall_json_data or self.overall_json_data.get('type') != 'overall':
            print("No valid 'overall' data found in the new JSON.")
            return
        
        data = self.overall_json_data.get('data', {})
        df = pd.DataFrame([(k, v['Validation']) for k, v in data.items()], columns=['Metric', 'Value'])
        
        if overall_args:
            if 'metrics' in overall_args:
                df = df[df['Metric'].isin(overall_args['metrics'])]
            if 'threshold' in overall_args:
                df = df[df['Value'] > overall_args['threshold']]
        
        df = df.sort_values('Value', ascending=False)
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Value', y='Metric', hue='Metric', data=df, palette='viridis')
        plt.title('Overall Metrics', fontsize=16)
        plt.xlabel('Value', fontsize=12)
        plt.ylabel('Metric', fontsize=12)
        for i, v in enumerate(df['Value']):
            plt.text(v, i, f' {v:.4f}', va='center')
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        else:
            plt.savefig('overall_metrics.png')
        plt.show()
        plt.close()


    def _plot_top_misses(self, top_misses_args, save_path):
        if not self.new_json_data or self.new_json_data.get('type') != 'image':
            print("No valid 'image' data found in the new JSON.")
            return
        
        data = self.new_json_data.get('data', [])
        df = pd.DataFrame(data)
        
        if top_misses_args:
            if 'min_miou' in top_misses_args:
                df = df[df['mIoU'] >= top_misses_args['min_miou']]
            if 'max_miou' in top_misses_args:
                df = df[df['mIoU'] <= top_misses_args['max_miou']]
            if 'top_n' in top_misses_args:
                df = df.nsmallest(top_misses_args['top_n'], 'rank')

        df = df.sort_values('rank')
        plt.figure(figsize=(12, 8))
        sns.barplot(x='mIoU', y='image_id', hue='image_id', data=df, palette='viridis')
        plt.title('mIoU for Each Image', fontsize=16)
        plt.xlabel('mIoU', fontsize=12)
        plt.ylabel('Image ID', fontsize=12)
        for i, v in enumerate(df['mIoU']):
            plt.text(v, i, f' {v:.4f}', va='center')
        if save_path:
            plt.savefig(save_path)
        else:
            plt.savefig('top_misses.png')
        plt.show()
        plt.close()


    def _plot_classbased_table_metrics(self,classbased_table_args, save_path):
        if not self.table_json_data or self.table_json_data.get('type') != 'table':
            print("No valid 'table' data found in the new JSON.")
            return
        
        data = self.table_json_data.get('data', {}).get('Validation', {})
        df = pd.DataFrame.from_dict(data, orient='index')
        
        if classbased_table_args:
            if 'metrics' in classbased_table_args:
                df = df[classbased_table_args['metrics']]
            if 'threshold' in classbased_table_args:
                df = df[df.apply(lambda row: all(float(val) > classbased_table_args['threshold'] for val in row if val != "None"), axis=1)]
        
        df = df.reset_index().rename(columns={'index': 'Class'})
        df = df.melt(id_vars=['Class'], var_name='Metric', value_name='Value')
        df['Value'] = df['Value'].astype(float)
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Value', y='Class', hue='Class', data=df, palette='viridis')
        plt.title('Table Metrics', fontsize=16)
        plt.xlabel('Value', fontsize=12)
        plt.ylabel('Class', fontsize=12)
        plt.legend(title='Metric')
        if save_path:
            plt.savefig(save_path)
        else:
            plt.savefig('table_metrics.png')
        plt.show()
        plt.close()
#histogram_save_path = save_path.replace('.png', '_histogram.png') if save_path else 'histogram.png'


    def _plot_mixed_metrics(self, mixed_args, save_path):
        if not self.mixed_json_data or self.mixed_json_data.get('type') != 'mixed':
            print("No valid 'mixed' data found in the new JSON.")
            return
        
        data = self.mixed_json_data.get('data', {}).get('ap_results', {})
        df = pd.DataFrame.from_dict(data, orient='index').reset_index().rename(columns={'index': 'Metric', 0: 'Value'})
        df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

        if mixed_args:
            if 'metrics' in mixed_args:
                df = df[df['Metric'].isin(mixed_args['metrics'])]
            if 'threshold' in mixed_args:
                df = df[df['Value'] > mixed_args['threshold']]
        
        plt.figure(figsize=(12, 8))
        sns.barplot(x='Value', y='Metric', data=df, hue='Metric', palette='viridis', dodge=False, legend=False)
        plt.title('Mixed Metrics', fontsize=16)
        plt.xlabel('Value', fontsize=12)
        plt.ylabel('Metric', fontsize=12)
        for i, v in enumerate(df['Value']):
            if pd.notna(v):
                plt.text(v, i, f' {v:.4f}', ha='center')
        if save_path:
            plt.savefig(save_path)
        else:
            plt.savefig('mixed_metrics.png')
        plt.show()
        plt.close()

    def _plot_confidence_histogram(self, confidence_histogram_args, save_path):
        if not self.confidence_histogram_data or self.confidence_histogram_data.get('type') != 'mixed':
            print("No valid 'confidence_histogram' data found in the new JSON.")
            return
        
        points_data = self.confidence_histogram_data.get('data', {}).get('points', [])
        histogram_data = self.confidence_histogram_data.get('data', {}).get('histogram', [])
        points_df = pd.DataFrame(points_data)
        histogram_df = pd.DataFrame(histogram_data)
        
        if confidence_histogram_args:
            if 'labels' in confidence_histogram_args:
                points_df = points_df[points_df['labels'].isin(confidence_histogram_args['labels'])]
        
        # Scatter plot of points
        plt.figure(figsize=(12, 8))
        sns.scatterplot(x='x', y='y', hue='labels', data=points_df, palette='viridis')
        plt.title('Scatter Plot of Points', fontsize=16)
        plt.xlabel('X', fontsize=12)
        plt.ylabel('Y', fontsize=12)
        plt.legend(title='Labels')
        scatter_save_path = save_path.replace('.png', '_scatter.png') if save_path else 'scatter_plot_points.png'
        plt.savefig(scatter_save_path)
        plt.show()
        plt.close()

        # Histogram
        plt.figure(figsize=(12, 8))
        sns.barplot(x='category', y='value', hue='value', data=histogram_df, palette='viridis')
        plt.title('Histogram', fontsize=16)
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Value', fontsize=12)
        histogram_save_path = save_path.replace('.png', '_histogram.png') if save_path else 'histogram.png'
        plt.savefig(histogram_save_path)
        plt.show()
        plt.close()