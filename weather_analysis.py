import json
import matplotlib.pyplot as plt


def load_weather_data(filepath):
    """ Load weather data from a JSON file. """
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def plot_temperature_trends(data, save_path="temperature_trends.png"):
    """ Plot daily max and min temperature over time. """
    daily = data["daily"]
    dates = daily["time"]
    temp_max = daily["temperature_2m_max"]
    temp_min = daily["temperature_2m_min"]
 
    plt.figure(figsize=(12, 5))
    plt.plot(dates, temp_max, label="Max Temp (°C)", color="tab:red")
    plt.plot(dates, temp_min, label="Min Temp (°C)", color="tab:blue")
    plt.fill_between(dates, temp_min, temp_max, color="gray", alpha=0.15)
 
    plt.title(f"Daily Temperature Range — {data.get('location_name', 'Unknown location')}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45, fontsize=7)
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Saved: {save_path}")



def plot_precipitation_and_humidity(data, save_path="precip_humidity.png"):
    """ Plot daily precipitation (bar) and mean humidity (line, secondary axis). """
    daily = data["daily"]
    dates = daily["time"]
    precip = daily["precipitation_sum"]
    humidity = daily["relative_humidity_2m_mean"]
 
    fig, ax1 = plt.subplots(figsize=(12, 5))
 
    ax1.bar(dates, precip, color="tab:blue", alpha=0.6, label="Precipitation (mm)")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Precipitation (mm)", color="tab:blue")
    ax1.tick_params(axis="y", labelcolor="tab:blue")
    ax1.set_xticks(range(len(dates)))
    ax1.set_xticklabels(dates, rotation=45, fontsize=7)
 
    ax2 = ax1.twinx()
    ax2.plot(dates, humidity, color="tab:green", label="Humidity (%)")
    ax2.set_ylabel("Relative Humidity (%)", color="tab:green")
    ax2.tick_params(axis="y", labelcolor="tab:green")
 
    plt.title(f"Precipitation & Humidity — {data.get('location_name', 'Unknown location')}")
    fig.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"Saved: {save_path}")


def main():
    filepath = "dataset.json"
    data = load_weather_data(filepath)
    plot_temperature_trends(data)
    plot_precipitation_and_humidity(data)

def hello():
    print("Experimenting")


if __name__ == "__main__":
    main()