# 1 Baye's Rule Application : Probability of a student absent on friday 
#    when probability of absent is 0.03 and probability of friday is 0.2

def bayes_rule(a, b):
    return a / b * 100

if __name__ == "__main__":
    friday_prob = 0.2
    absent_friday_prob = 0.03
    print(bayes_rule(absent_friday_prob, friday_prob))