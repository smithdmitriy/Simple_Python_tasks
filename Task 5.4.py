salutation = 'Mr.'
name = 'Putin'
product = 'knive'
verbed = 'HZ'
room = 'kitchen'
animals = 'horse'
percent = '99'
spokesman = 'Barak Obama'
job_title = 'President'
amount = "$500"

print("Dear %s %s," % (salutation, name),
      "Thank you for your letter. We are sorry that our %s" % product,
      "%s in your %s. Please note that it should never" % (verbed, room),
      "be used in a %s, especially near any %s." % (room, animals),
      "is %s %% less likely to have %s." % (percent, verbed),
      "Send us your receipt and %s for shipping and handling." % amount,
      "We will send you another %s that, in our tests," % product,
      "Thank you for your support.",
      "Sincerely,",
      "%s" % spokesman,
      "%s" % job_title,
      sep='\n')

print()

print("Dear {} {},".format(salutation, name),
      "Thank you for your letter. We are sorry that our {}".format(product),
      "{} in your {}. Please note that it should never".format(verbed, room),
      "be used in a {}, especially near any {}.".format(room, animals),
      "Send us your receipt and {} for shipping and handling.".format(amount),
      "We will send you another {} that, in our tests,".format(product),
      "is {}% less likely to have {}.".format(percent, verbed),
      "Thank you for your support.",
      "Sincerely,",
      "{}".format(spokesman),
      "{}".format(job_title),
      sep='\n')

print()

print(f"Dear {salutation} {name},",
f"Thank you for your letter. We are sorry that our {product}",
f"{verbed} in your {room}. Please note that it should never",
f"be used in a {room}, especially near any {animals}.",
f"Send us your receipt and {amount} for shipping and handling.",
f"We will send you another {product} that, in our tests,",
f"is {percent}% less likely to have {verbed}.",
f"Thank you for your support.",
f"Sincerely,",
f"{spokesman}",
f"{job_title}",
sep="\n")
