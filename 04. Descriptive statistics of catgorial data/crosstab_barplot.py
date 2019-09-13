'''
create a function to show pie chart based on categorial crosstab
'''
def crosstab_barplot() :
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline

    crosstab = categorial_crosstab()
    trait = input('Whict trait to show ? ')
    a = list(crosstab['Category'][crosstab['Trait']==trait])
    objects = a[0]
    y_pos = np.arange(len(objects))
    b = list(crosstab['Freq'][crosstab['Trait']==trait])
    performance = b[0]

    plt.barh(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_pos, objects)
    plt.xlabel('Frequency')
    plt.ylabel('Category')
    plt.title('Frequency Distribution of trait {}' .format(trait))

    result = plt.show()
    print (result)
    return result
