from weather import describe_weather

def test_weather_decription():
    result = describe_weather()
    assert result in ["Freezing", "Cold", "Pleasant", "Hot"]

    