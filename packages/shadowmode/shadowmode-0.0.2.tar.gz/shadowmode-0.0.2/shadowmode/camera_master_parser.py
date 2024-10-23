import pandas as pd
from pandas import DataFrame
from collections import defaultdict
import json
import re


class CameraMasterParser():
    def __init__(self, config_path:str, camera_master_path:str):
        self.data_info = json.loads(open(f'{config_path}', 'r').read())
        self.trigger_pattern = r"Evaluated to true"
        self.data_dict = {}
        self._initialize_dataFrame()
        self.camera_master_path = camera_master_path

    def _initialize_dataFrame(self) -> None:
        self.data_dict['time_stamp'] = []
        for column in self.data_info['columns'].keys():
           self.data_dict[column] = []
        self.data_dict['trigger'] = []

    def _initialize_newrow(self, timestamp) -> None:
        for column in self.data_info['columns'].keys():
            if self.data_info['columns'][column] == "Array":
                self.data_dict[column].append([])
            else :
                self.data_dict[column].append(None)
        self.data_dict['trigger'].append(False)
    
    def _extract_columns(self, log_line):
        time_stamp = re.findall(r"\d+us", log_line)[0]
        if not self.data_dict['time_stamp'] or self.data_dict['time_stamp'][-1] != time_stamp:
            self.data_dict['time_stamp'].append(time_stamp)
            self._initialize_newrow(time_stamp)
        current_timestamp_index = len(self.data_dict['time_stamp']) - 1
        for column in self.data_dict.keys():
            if column == 'time_stamp':
                continue
            elif column == "trigger":
                if re.search(self.trigger_pattern, log_line):
                    self.data_dict['trigger'][current_timestamp_index] = True
            
            elif self.data_info['columns'][column] == "Array":
                data_array_match = re.search(column, log_line)
                if data_array_match:
                    self.data_dict[column][current_timestamp_index].append(log_line[data_array_match.end():].strip("\n"))
            else:
                data_match = re.search(column,log_line)
                if data_match:
                    self.data_dict[column][current_timestamp_index]=log_line[data_match.end():].strip("\n")
    
    def get_dataFrame(self) -> DataFrame:
        try:
            with open(self.camera_master_path, "r") as f:
                log_lines = f.readlines()
        except KeyError:
            print("Error: Check the file path of camera_master.log specified ")
        for line in log_lines:
            if re.search(self.data_info['EvaluatorName'], line):
                self._extract_columns(line)
        return pd.DataFrame(self.data_dict)