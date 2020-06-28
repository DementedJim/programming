import pandas  # импортирование библиотеки для считывания данных

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


def get_sex_distrib(data):
    """
    Количество мужчин и женщин пароходе.
    """
    data = pandas.read_csv(data, index_col="PassengerId")

    n_male, n_female = 0, 0
    res = data['Sex'].value_counts()

    n_male, n_female = res['male'], res['female']

    return n_male, n_female
print( get_sex_distrib('train.csv') )



def get_port_distrib(data):
    """  
    Количество пассажиров, которое загрузилось на борт в различных портах.
    """
    data = pandas.read_csv(data, index_col="PassengerId")

    port_S, port_C, port_Q = 0, 0, 0
    res = data['Embarked'].value_counts()

    port_S, port_C, port_Q = res['S'], res['C'], res['Q']
    return port_S, port_C, port_Q
print( get_port_distrib('train.csv') )



def get_surv_percent(data):
    """
    Доля погибших на пароходе (число и процент).
    """
    data = pandas.read_csv(data, index_col="PassengerId")

    n_died, perc_died = 0, 0

    res = data['Survived'].value_counts()
    n_died, perc_died = res[0], 100 * (res[0] / (res[1] + res[0]))

    return n_died, perc_died


print(get_surv_percent('train.csv'))



def get_class_distrib(data):
    """
    Доли пассажиров первого, второго, третьего классов.    
    """
    # n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0

    res = data['Pclass'].value_counts()

    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = (res[1]/(res[1]+res[2]+res[3])), (res[2]/(res[1]+res[2]+res[3])), (res[3]/(res[1]+res[2]+res[3]))

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl

print(get_class_distrib(data))



def find_corr_age_survival(data):
    """
    Корреляция (коэффициент корреляции Пирсона) между:

    - возрастом и параметром survival;

    """

    age = data['Age']
    #print(sibsp)
    surv = data['Survived']
    #print(parch)

    corr_val = age.corr(surv, method='pearson')
    return corr_val
print(find_corr_age_survival(data))


'''
Есть ли корреляция (коэффициент корреляции Пирсона) между:

    - полом человека и параметром survival; ?
    
    
Нет корреляции.
'''



def find_corr_class_survival(data):
    """
    Корреляция (коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """
    pclass = data['Pclass']
    surv = data['Survived']

    corr_val = pclass.corr(surv, method='pearson')
    return corr_val
print (find_corr_class_survival(data))


def find_pass_mean_median(data):
    """
    Средний возраст пассажиров и медиана.
    """
    age = data['Age']

    mean_age, median = age.mean(), age.median()
    return mean_age, median

print(find_pass_mean_median(data))


def find_ticket_mean_median(data):
    """
    Средняя цена за билет и медиана.
    """

    price = data['Fare']

    mean_price, median = price.mean(), price.median()
    return mean_price, median
print (find_ticket_mean_median(data))


def get_name(name):


#Определение имени


    import re
    fam = re.search('^[^,]+, (.*)', name)
    if fam:
        name = fam.group(1)
    fam = re.search('\(([^)]+)\)', name)
    if fam:
        name = fam.group(1)
    name = re.sub('(Master\. |Mr\. |Mrs\. |Miss\. )', '', name)
    name = name.split(' ')[0].replace('"', '')
    return name

def get_favorite_name(dataset,sex,age):

#Популярное имя в возрастной категории

    if (dataset is None):
        return ''
    names = dataset[data['Age'] > age]['Name'].map(get_name)
    #print(names)
    if (sex=='male' or sex=='female'):
        names = dataset[data['Sex'] == sex][data['Age'] > age]['Name'].map(get_name)
    name_counts = names.value_counts()
    if(name_counts.count()>0):
        return name_counts.head(1).index.values[0]
    return ''

print('Самые популярные имена у мужчин старше 15 лет')
print(get_favorite_name(data,'male',15))
print('Самые популярные имена у женщин старше 15 лет')
print(get_favorite_name(data,'female',15))
print('Самые популярные имена среди всех пассажиров старше 15 лет')
print(get_favorite_name(data,'',15))
