import speedtest

test_obj = speedtest.Speedtest()

# print("Downloading speed ", test_obj.download())
print("Upload speed ", test_obj.upload())
