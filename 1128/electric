from abc import ABC, abstractmethod
electricity_usage = [
    {"date": "2024-11-01", "usage": 12.5},
    {"date": "2024-11-02", "usage": 15.3},
    {"date": "2024-11-03", "usage": 10.8},
    {"date": "2024-11-04", "usage": 14.2},
    {"date": "2024-11-05", "usage": 13.6}
]


class ElectricityData(ABC):
    def __init__(self, usage_data):
        self._usage_data = usage_data
        self._total_usage = 0

    @property
    def usage_data(self):
        return self._usage_data

    @usage_data.setter
    def usage_data(self, value):
        self._usage_data = value

    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self, value):
        self._total_usage = value

    @abstractmethod
    def calc_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        new_data = {"date": date, "usage": usage}
        self._usage_data.append(new_data)
        self.total_usage = self.calc_total_usage()
        return (f"{date} 추가 후 총 전력 사용량 : {self.total_usage}")

    def remove_usage(self, date):
        for data in self._usage_data:
            if data["date"] == date:
                self._usage_data.remove(data)
                self.total_usage = self.calc_total_usage()
                return f"{date}의 전력 사용량 {data['usage']} 삭제 후 총 사용량: {self.total_usage}"
        return f"{date}의 데이터가 없습니다."

    @classmethod
    def date_filter(cls, usage_data, start, end):
        filtered_date = [
            data for data in usage_data if start <= data["date"] <= end]
        if filtered_date:
            return f"특정 범위 내 사용량 : {filtered_date}"
        else:
            return f"{start}부터 {end}까지의 데이터가 존재하지 않습니다."


class HomeElectricityData(ElectricityData):
    def __init__(self, usage_data):
        super().__init__(usage_data)

    def calc_total_usage(self):
        return sum(data["usage"] for data in self._usage_data)

    def get_usage_on_date(self, date):
        for data in self.usage_data:
            if data["date"] == date:
                selected_date = data["usage"]
        return (f"{date}의 사용량 : {selected_date}")


class Find:
    @staticmethod
    def find_max(usage_data):
        max_usage = max(usage_data, key=lambda x: x["usage"])
        return f"가장 높은 사용량: {max_usage}"


elec = HomeElectricityData(electricity_usage)
print(elec.calc_total_usage())
print(elec.get_usage_on_date("2024-11-03"))
print(elec.add_usage("2024-11-06", 16.4))
print(ElectricityData.date_filter(electricity_usage, "2024-11-02", "2024-11-04"))
print(Find.find_max(electricity_usage))
