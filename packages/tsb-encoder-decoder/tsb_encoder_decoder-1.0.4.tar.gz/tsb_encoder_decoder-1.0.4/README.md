### Python library for TSB
Taskit Serial Bus (TSB) is a packet protocol for serial data

e.g.: 
encoder_decoder = TSBEncoderDecoder()
tsb_msg = encoder_decoder.encode(0x01, encoder_decoder.TSB_TYPE_TEXT, "Hello, world!")
channel, tsb_type, payload = encoder_decoder.decode(tsb_msg)
print(channel, tsb_type, payload)