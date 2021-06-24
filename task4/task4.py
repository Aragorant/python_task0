import telebot
import config
import http.client

text1=''
text2=''
text3=''
text4=''
text5=''
text6=''


conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
res = conn.getresponse()
data = res.read()
val = data.decode("utf-8")

    


def Infection_Risk(country):
    num = val.find('Infection_Risk',val.find(country))
    num2 = val.find('Case_Fatality_Rate',val.find(country))
    return val[num+16:num2-2]

def Case_Fatality_Rate(country):
    num = val.find('Case_Fatality_Rate',val.find(country))
    num2 = val.find('Test_Percentage',val.find(country))
    return val[num+20:num2-2]

def Total_Deaths(country):
    num = val.find('TotalDeaths',val.find(country))
    num2 = val.find('NewDeaths',val.find(country))
    return val[num+13:num2-2]

def Total_Tests(country):
    num = val.find('TotalTests',val.find(country))
    num2 = val.find('Population',val.find(country))
    return val[num+13:num2-3]

def Population(country):
    num = val.find('Population',val.find(country))
    num2 = val.find('one_Caseevery_X_ppl',val.find(country))
    return val[num+13:num2-3]





bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def lala(message):
    bot.send_message(message.chat.id, 'Country - France\nInfection Risk - ' + Infection_Risk('France') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('France') + '\nTotal Deaths - ' + Total_Deaths('France') + '\nTotal Tests - ' + Total_Tests('France') + '\nPopulation - ' + Population('France'))
    bot.send_message(message.chat.id, 'Country - Russia\nInfection Risk - ' + Infection_Risk('Russia') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Russia') + '\nTotal Deaths - ' + Total_Deaths('Russia') + '\nTotal Tests - ' + Total_Tests('Russia') + '\nPopulation - ' + Population('Russia'))
    bot.send_message(message.chat.id, 'Country - UK\nInfection Risk - ' + Infection_Risk('UK') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('UK') + '\nTotal Deaths - ' + Total_Deaths('UK') + '\nTotal Tests - ' + Total_Tests('UK') + '\nPopulation - ' + Population('UK'))
    bot.send_message(message.chat.id, 'Country - Italy\nInfection Risk - ' + Infection_Risk('Italy') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Italy') + '\nTotal Deaths - ' + Total_Deaths('Italy') + '\nTotal Tests - ' + Total_Tests('Italy') + '\nPopulation - ' + Population('Italy'))
    bot.send_message(message.chat.id, 'Country - Spain\nInfection Risk - ' + Infection_Risk('Spain') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Spain') + '\nTotal Deaths - ' + Total_Deaths('Spain') + '\nTotal Tests - ' + Total_Tests('Spain') + '\nPopulation - ' + Population('Spain'))
    global text1
    text1 = 'Country - France\nInfection Risk - ' + Infection_Risk('France') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('France') + '\nTotal Deaths - ' + Total_Deaths('France') + '\nTotal Tests - ' + Total_Tests('France') + '\nPopulation - ' + Population('France')
    global text2
    text2 = 'Country - Russia\nInfection Risk - ' + Infection_Risk('Russia') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Russia') + '\nTotal Deaths - ' + Total_Deaths('Russia') + '\nTotal Tests - ' + Total_Tests('Russia') + '\nPopulation - ' + Population('Russia')
    global text3
    text3 = 'Country - UK\nInfection Risk - ' + Infection_Risk('UK') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('UK') + '\nTotal Deaths - ' + Total_Deaths('UK') + '\nTotal Tests - ' + Total_Tests('UK') + '\nPopulation - ' + Population('UK')
    global text4
    text4 = 'Country - Italy\nInfection Risk - ' + Infection_Risk('Italy') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Italy') + '\nTotal Deaths - ' + Total_Deaths('Italy') + '\nTotal Tests - ' + Total_Tests('Italy') + '\nPopulation - ' + Population('Italy')
    global text5
    text5 = 'Country - Spain\nInfection Risk - ' + Infection_Risk('Spain') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Spain') + '\nTotal Deaths - ' + Total_Deaths('Spain') + '\nTotal Tests - ' + Total_Tests('Spain') + '\nPopulation - ' + Population('Spain') + '\n'

@bot.message_handler(commands=['update'])
def lala(message):
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")
    bot.send_message(message.chat.id, 'Country - France\nInfection Risk - ' + Infection_Risk('France') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('France') + '\nTotal Deaths - ' + Total_Deaths('France') + '\nTotal Tests - ' + Total_Tests('France') + '\nPopulation - ' + Population('France'))
    bot.send_message(message.chat.id, 'Country - Russia\nInfection Risk - ' + Infection_Risk('Russia') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Russia') + '\nTotal Deaths - ' + Total_Deaths('Russia') + '\nTotal Tests - ' + Total_Tests('Russia') + '\nPopulation - ' + Population('Russia'))
    bot.send_message(message.chat.id, 'Country - UK\nInfection Risk - ' + Infection_Risk('UK') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('UK') + '\nTotal Deaths - ' + Total_Deaths('UK') + '\nTotal Tests - ' + Total_Tests('UK') + '\nPopulation - ' + Population('UK'))
    bot.send_message(message.chat.id, 'Country - Italy\nInfection Risk - ' + Infection_Risk('Italy') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Italy') + '\nTotal Deaths - ' + Total_Deaths('Italy') + '\nTotal Tests - ' + Total_Tests('Italy') + '\nPopulation - ' + Population('Italy'))
    bot.send_message(message.chat.id, 'Country - Spain\nInfection Risk - ' + Infection_Risk('Spain') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Spain') + '\nTotal Deaths - ' + Total_Deaths('Spain') + '\nTotal Tests - ' + Total_Tests('Spain') + '\nPopulation - ' + Population('Spain'))
    global text1
    text1 = 'Country - France\nInfection Risk - ' + Infection_Risk('France') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('France') + '\nTotal Deaths - ' + Total_Deaths('France') + '\nTotal Tests - ' + Total_Tests('France') + '\nPopulation - ' + Population('France')
    global text2
    text2 = 'Country - Russia\nInfection Risk - ' + Infection_Risk('Russia') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Russia') + '\nTotal Deaths - ' + Total_Deaths('Russia') + '\nTotal Tests - ' + Total_Tests('Russia') + '\nPopulation - ' + Population('Russia')
    global text3
    text3 = 'Country - UK\nInfection Risk - ' + Infection_Risk('UK') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('UK') + '\nTotal Deaths - ' + Total_Deaths('UK') + '\nTotal Tests - ' + Total_Tests('UK') + '\nPopulation - ' + Population('UK')
    global text4
    text4 = 'Country - Italy\nInfection Risk - ' + Infection_Risk('Italy') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Italy') + '\nTotal Deaths - ' + Total_Deaths('Italy') + '\nTotal Tests - ' + Total_Tests('Italy') + '\nPopulation - ' + Population('Italy')
    global text5
    text5 = 'Country - Spain\nInfection Risk - ' + Infection_Risk('Spain') + '\nCase Fatality Rate - ' + Case_Fatality_Rate('Spain') + '\nTotal Deaths - ' + Total_Deaths('Spain') + '\nTotal Tests - ' + Total_Tests('Spain') + '\nPopulation - ' + Population('Spain') + '\n'






@bot.message_handler(commands=['help'])
def lala(message):
    bot.send_message(message.chat.id, '/start - shows statistics of 5 countries\n/update - update statistics of 5 countries\n/show [country] - shows [country] statistics\n/save - save data to text.txt')

@bot.message_handler(commands=['show'])
def lala(message):
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "a0580e8b98mshde852a61dc71befp1f85d5jsne85be2246ec5",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    val = data.decode("utf-8")
    tex = message.text
    tex = tex[6:]
    if (val.find(tex)) == -1:
        bot.send_message(message.chat.id, 'Country - Doesn\'t exist')
    else:
        bot.send_message(message.chat.id, 'Country - ' + tex + '\nInfection Risk - ' + Infection_Risk(tex) + '\nCase Fatality Rate - ' + Case_Fatality_Rate(tex) + '\nTotal Deaths - ' + Total_Deaths(tex) + '\nTotal Tests - ' + Total_Tests(tex) + '\nPopulation - ' + Population(tex))
    global text6
    text6 = 'Country - ' + tex + '\nInfection Risk - ' + Infection_Risk(tex) + '\nCase Fatality Rate - ' + Case_Fatality_Rate(tex) + '\nTotal Deaths - ' + Total_Deaths(tex) + '\nTotal Tests - ' + Total_Tests(tex) + '\nPopulation - ' + Population(tex)

@bot.message_handler(commands=['save'])
def lala(message):
    f = open('text.txt', 'w')
    f.write(text1)
    f.write(text2)
    f.write(text3)
    f.write(text4)
    f.write(text5)
    f.write(text6)
    f.close()
    file = open('text.txt', 'rb')
    bot.send_document(message.chat.id, file)
    file.close()



@bot.message_handler(content_types=['text'])
def lala(message):
    bot.send_message(message.chat.id, 'Unknown command\nTo find out the commands write /help')

    
bot.polling(none_stop=True)































