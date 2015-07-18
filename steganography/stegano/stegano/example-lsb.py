import slsb

secret = slsb.hide("../examples/pictures/Lenna.png", "message")
secret.save("Lenna-secret.png")
print(slsb.reveal("Lenna-secret.png"))
