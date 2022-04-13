import matplotlib.pyplot as plt

def generate(data):
    labels = [1,2,3,4,5,6]
    plt.bar(range(0,6),data, tick_label=labels)
    plt.savefig('stats.png')

if __name__ == "__main__":
    generate([3,10,4,5,6,1])
