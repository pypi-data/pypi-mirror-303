from enum import Enum, auto
import regex
from os.path import dirname
import types
from typing import Union, List, Tuple, Dict, cast, TypedDict
import csv

def load_designator_data():
    # read csv file as txt
    # return list of tuples with pattern and sidc
    path = f"{dirname(__file__)}/patterns_data.csv"
    open_file = open(path, "r", encoding="utf-8")
    lines = open_file.readlines()
    open_file.close()

    # create list of tuples and remove new line character
    data = []
    for line in lines:
        pattern, sidc = line.strip().split(",")
        data.append((pattern, sidc))

    return data

class PatternDict(TypedDict):
    sidc: str
    list_of_patterns: List[str]


def parse_csv_to_dict_list(file_path: str) -> List[PatternDict]:
    result: List[PatternDict] = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != "sidc":
                sidc, pattern_str = row[0], row[1]
                patterns: List[str] = cast(List[str], pattern_str.split('|'))
                result.append({"sidc": sidc, "list_of_patterns": patterns}) 
    return result


class Status(Enum):
    """
    Provides status of the unit.
    """
    PRESENT = "0"
    PLANNED_ANTICIPATED_SUSPECT = "1"
    FULLY_CAPABLE = "2"
    DAMAGED = "3" 
    DESTROYED = "4"
    FULL_TO_CAPACITY = "5"

class Mobility(Enum):
    """
    Provides mobility of the unit. 
    """
    UNSPECIFIED = auto()
    WHEELED_LIMITED_CROSS_COUNTRY = auto()
    WHEELED_CROSS_COUNTRY = auto()
    TRACKED = auto()
    WHEELED_AND_TRACKED_COMBINATION = auto()
    TOWED = auto()

class Matched:
    def __init__(self, sidc: str, pattern: str, matched_text: str):
        self.sidc = sidc
        self.pattern = pattern
        self.matched_text = matched_text

    def set_mobility(self, sidc: str, mobility: Mobility) -> None:
        """
        Set's mobility for disignated unit
        """
        if mobility == Mobility.WHEELED_LIMITED_CROSS_COUNTRY:
            self.set_char_at_position(sidc, '3', 8)
            self.set_char_at_position(sidc, '1', 9)
        elif mobility == Mobility.WHEELED_CROSS_COUNTRY:
            self.set_char_at_position(sidc, '3', 8)
            self.set_char_at_position(sidc, '2', 9)
        elif mobility == Mobility.TRACKED:
            self.set_char_at_position(sidc, '3', 8)
            self.set_char_at_position(sidc, '3', 9)
        elif mobility == Mobility.TOWED:
            self.set_char_at_position(sidc, '3', 8)
            self.set_char_at_position(sidc, '5', 9)
        else:  # Mobility.UNSPECIFIED or any other case
            self.set_char_at_position(sidc, '0', 8)
            self.set_char_at_position(sidc, '0', 9)
        # return sidc

    def set_char_at_position(self, sidc: str, character: str, position: int) -> None:
        "Replaces characters by gives ones"
        replacement = list(sidc)
        replacement[position] = character
        self.sidc = "".join(replacement)


class UnitDesignator:
    """
    Accepts a name of the unit and returns a SIDC code.
    """
    default_sidc = "10012500001313000000"
    _data: List[Tuple[str, str]] = load_designator_data()

    @staticmethod
    def calculate_icon(name: str) -> Matched:
        return UnitDesignator.calculate_icon_with_flag(name, True)

    @staticmethod
    def calculate_icon_with_flag(name: str, calculate_icon: bool) -> Matched:
        if calculate_icon and name:
            matched_values = UnitDesignator.get_unit(name)

            if matched_values is None:
                return Matched(sidc=UnitDesignator.default_sidc, pattern="", matched_text="")
            else:
                return matched_values
        else:
            return Matched(sidc=UnitDesignator.default_sidc, pattern="", matched_text="")

    @staticmethod
    def get_unit(name: str) -> Union[Matched, None]:
        mobility = Mobility.UNSPECIFIED
        if "БУКСИРОВАНИЙ" in name:
            mobility = Mobility.TOWED
            name = name.replace("БУКСИРОВАНИЙ", "")

        matched_values = UnitDesignator.designate_icon(name)


        if matched_values is None:
            return None


        if any(keyword in name for keyword in ["МАКЕТ", "МУЛЯЖ", "МАКЕТЫ", "МУЛЯЖИ", "МАКЕТА", "МУЛЯЖА"]):
            matched_values.set_char_at_position(matched_values.sidc, "1", 7)
            return matched_values

        if any(keyword in name for keyword in ["УРАЖЕНО", "УРАЖЕНА", "ПОШКОДЖЕНА", "ПОШКОДЖЕНО", "ПОШКОДЖЕНІ", 
                                            "ПОРАЖЕНО", "ПОРАЖЕНА", "ПОВРЕЖДЕНА", "ПОВРЕЖДЕНО", "ПОВРЕЖДЕННЫЕ"]):
            if matched_values is not None:
                matched_values.set_char_at_position(matched_values.sidc, Status.DAMAGED.value, 6)
                return matched_values


        if any(keyword in name for keyword in ["ЗНИЩЕНОГО", "ЗНИЩЕНА", "ЗРУЙНОВАНО", "ЗНИЩЕНО",
                                            "УНИЧТОЖЕННОГО", "УНИЧТОЖЕНА", "РАЗРУШЕНО", "УНИЧТОЖЕНО"]):
            
            if matched_values is not None:
                matched_values.set_char_at_position(matched_values.sidc, Status.DESTROYED.value, 6)
                return matched_values

        if "ВІДНОВЛЕНО" in name:
            if matched_values is not None:
                matched_values.set_char_at_position(matched_values.sidc, Status.FULL_TO_CAPACITY.value, 6)
                return matched_values

        if any(keyword in name for keyword in ["ЙМОВІРНО", "МОЖЛИВО", "ЙМОВІРНА",
                                              "ВЕРОЯТНО", "ВОЗМОЖНО", "ВЕРОЯТНАЯ"]):
            if matched_values is not None:
                matched_values.set_char_at_position(matched_values.sidc, Status.PLANNED_ANTICIPATED_SUSPECT.value, 6)
                return matched_values

        if  mobility != Mobility.UNSPECIFIED and matched_values.sidc is not None:
            matched_values.set_mobility(matched_values.sidc, mobility)
            return matched_values

        return matched_values

    @staticmethod
    def additional_pattern(pattern):
            return (r'(^|[^\p{L}])' + "(" + pattern + ")" + r'($|[^\p{L}])')
    


    @staticmethod
    def designate_icon(name: str) -> Union[None, Matched]:  
        for pattern_row in UnitDesignator._data:
            full_pattern = UnitDesignator.additional_pattern(pattern_row[1])
            
            match = regex.search(full_pattern, name, flags=regex.IGNORECASE)            
            if match:
                full_match = match.group()
                return Matched(sidc=pattern_row[0], matched_text=full_match, pattern=pattern_row[1])
        return None 
    
    @classmethod
    def transoform_patterns(cls, patterns: List[PatternDict]) -> List[Tuple[str, str]]:
        return [ (pat['sidc'], "|".join(pat['list_of_patterns']))  for pat in patterns]

    
    @staticmethod
    def import_custom_patterns(list_of_dicts: List[PatternDict]):
        transformed_patterns = UnitDesignator.transoform_patterns(list_of_dicts)

        # Insert all elements at the beginning of the list
        UnitDesignator._data = transformed_patterns + UnitDesignator._data


    @staticmethod
    def set_default_sidc(default_sidc: str):
        UnitDesignator.default_sidc = default_sidc

