import speedtest
'''
pip install speedtest-cli
'''

test_rede = speedtest.Speedtest()
download = test_rede.download()
upload = test_rede.upload()

print(f'Donwload speed: {download}')
print(f'Upload speed: {upload}')
