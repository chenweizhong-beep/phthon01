import yaml


class Bicycle():
    def run(self, km):
        print(f"骑行里程数为：{km}千米")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        self.battery_level = battery_level

    def fill_charge(self, vol):
        self.battery_level = self.battery_level + vol
        print(f"当前电量为：{self.battery_level}")

    def run(self, km):
        miles = km - self.battery_level * 10
        if miles > 0:
            print(f"用电行驶了{self.battery_level * 10}千米")
            super().run(miles)
        else:
            print(f"用电行驶了{km}千米")
            print(f"剩余电量为：{self.battery_level - km / 10}")


if __name__ == '__main__':
    # eb = EBicycle(10)
    # eb.fill_charge(5)
    # eb.run(120)
    with open('bicycle_config.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas['deafult'])
    battety_lecel = datas['deafult']['battery_level']
    vol = datas['deafult']['vol']
    run_km = datas['deafult']['run_km']
    eb = EBicycle(battety_lecel)
    eb.fill_charge(vol)
    eb.run(run_km)

