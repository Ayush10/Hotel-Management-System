def discount(self):
    if TT > 50000:
        customerCategory = "Gold"
    elif TT > 30000 && TT <= 50000:
        customerCategory = "Silver"
    elif TT > 15000 && TT <= 30000:
        customerCategory = "Bronze"
    elif TT <= 15000:
        customerCategory = "Normal"