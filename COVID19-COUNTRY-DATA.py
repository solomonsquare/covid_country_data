from tkinter import *
import requests
#import pycountry as pc
import json
from tkinter import messagebox

HEIGHT = 700
WIDTH = 800



def get_news(entry):
 
    Country = {
    'US':'Usa',
    'AF':'Afghanistan',
    'AL': 'Albania',
    'DZ': 'Algeria',
    'AS': 'American Samoa',
    'AD': 'Andorra',
    'AO': 'Angola',
    'AI': 'Anguilla',
    'AQ': 'Antarctica',
    'AG': 'Antigua And Barbuda',
    'AR': 'Argentina',
    'AM': 'Armenia',
    'AW': 'Aruba',
    'AU': 'Australia',
    'AT': 'Austria',
    'AZ': 'Azerbaijan',
    'BS': 'Bahamas',
    'BH': 'Bahrain',
    'BD': 'Bangladesh',
    'BB': 'Barbados',
    'BY': 'Belarus',
    'BE': 'Belgium',
    'BZ': 'Belize',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BT': 'Bhutan',
    'BO': 'Bolivia',
    'BA': 'Bosnia And Herzegowina',
    'BW': 'Botswana',
    'BV': 'Bouvet Island',
    'BR': 'Brazil',
    'BN': 'Brunei Darussalam',
    'BG': 'Bulgaria',
    'BF': 'Burkina Faso',
    'BI': 'Burundi',
    'KH': 'Cambodia',
    'CM': 'Cameroon',
    'CA': 'Canada',
    'CV': 'Cape Verde',
    'KY': 'Cayman Islands',
    'CF': 'Central African Rep',
    'TD': 'Chad',
    'CL': 'Chile',
    'CN': 'China',
    'CX': 'Christmas Island',
    'CC': 'Cocos Islands',
    'CO': 'Colombia',
    'KM': 'Comoros',
    'CG': 'Congo',
    'CK': 'Cook Islands',
    'CR': 'Costa Rica',
    'CI': 'Cote D`ivoire',
    'HR': 'Croatia',
    'CU': 'Cuba',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DK': 'Denmark',
    'DJ': 'Djibouti',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'TP': 'East Timor',
    'EC': 'Ecuador',
    'EG': 'Egypt',
    'SV': 'El Salvador',
    'GQ': 'Equatorial Guinea',
    'ER': 'Eritrea',
    'EE': 'Estonia',
    'ET': 'Ethiopia',
    'FK': 'Falkland Islands (Malvinas)',
    'FO': 'Faroe Islands',
    'FJ': 'Fiji',
    'FI': 'Finland',
    'FR': 'France',
    'GF': 'French Guiana',
    'PF': 'French Polynesia',
    'TF': 'French S. Territories',
    'GA': 'Gabon',
    'GM': 'Gambia',
    'GE': 'Georgia',
    'DE': 'Germany',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GR': 'Greece',
    'GL': 'Greenland',
    'GD': 'Grenada',
    'GP': 'Guadeloupe',
    'GU': 'Guam',
    'GT': 'Guatemala',
    'GN': 'Guinea',
    'GW': 'Guinea-bissau',
    'GY': 'Guyana',
    'HT': 'Haiti',
    'HN': 'Honduras',
    'HK': 'Hong Kong',
    'HU': 'Hungary',
    'IS': 'Iceland',
    'IN': 'India',
    'ID': 'Indonesia',
    'IR': 'Iran',
    'IQ': 'Iraq',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JP': 'Japan',
    'JO': 'Jordan',
    'KZ': 'Kazakhstan',
    'KE': 'Kenya',
    'KI': 'Kiribati',
    'KP': 'Korea (North)',
    'KR': 'Korea (South)',
    'KW': 'Kuwait',
    'KG': 'Kyrgyzstan',
    'LA': 'Laos',
    'LV': 'Latvia',
    'LB': 'Lebanon',
    'LS': 'Lesotho',
    'LR': 'Liberia',
    'LY': 'Libya',
    'LI': 'Liechtenstein',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'MO': 'Macau',
    'MK': 'Macedonia',
    'MG': 'Madagascar',
    'MW': 'Malawi',
    'MY': 'Malaysia',
    'MV': 'Maldives',
    'ML': 'Mali',
    'MT': 'Malta',
    'MH': 'Marshall Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MU': 'Mauritius',
    'YT': 'Mayotte',
    'MX': 'Mexico',
    'FM': 'Micronesia',
    'MD': 'Moldova',
    'MC': 'Monaco',
    'MN': 'Mongolia',
    'MS': 'Montserrat',
    'MA': 'Morocco',
    'MZ': 'Mozambique',
    'MM': 'Myanmar',
    'NA': 'Namibia',
    'NR': 'Nauru',
    'NP': 'Nepal',
    'NL': 'Netherlands',
    'AN': 'Netherlands Antilles',
    'NC': 'New Caledonia',
    'NZ': 'New Zealand',
    'NI': 'Nicaragua',
    'NE': 'Niger',
    'NG': 'Nigeria',
    'NU': 'Niue',
    'NF': 'Norfolk Island',
    'MP': 'Northern Mariana Islands',
    'NO': 'Norway',
    'OM': 'Oman',
    'PK': 'Pakistan',
    'PW': 'Palau',
    'PA': 'Panama',
    'PG': 'Papua New Guinea',
    'PY': 'Paraguay',
    'PE': 'Peru',
    'PH': 'Philippines',
    'PN': 'Pitcairn',
    'PL': 'Poland',
    'PT': 'Portugal',
    'PR': 'Puerto Rico',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'KN': 'Saint Kitts And Nevis',
    'LC': 'Saint Lucia',
    'VC': 'St Vincent/Grenadines',
    'WS': 'Samoa',
    'SM': 'San Marino',
    'ST': 'Sao Tome',
    'SA': 'Saudi Arabia',
    'SN': 'Senegal',
    'SC': 'Seychelles',
    'SL': 'Sierra Leone',
    'SG': 'Singapore',
    'SK': 'Slovakia',
    'SI': 'Slovenia',
    'SB': 'Solomon Islands',
    'SO': 'Somalia',
    'ZA': 'South Africa',
    'ES': 'Spain',
    'LK': 'Sri Lanka',
    'SH': 'St. Helena',
    'PM': 'St.Pierre',
    'SD': 'Sudan',
    'SR': 'Suriname',
    'SZ': 'Swaziland',
    'SE': 'Sweden',
    'CH': 'Switzerland',
    'SY': 'Syrian Arab Republic',
    'TW': 'Taiwan',
    'TJ': 'Tajikistan',
    'TZ': 'Tanzania',
    'TH': 'Thailand',
    'TG': 'Togo',
    'TK': 'Tokelau',
    'TO': 'Tonga',
    'TT': 'Trinidad And Tobago',
    'TN': 'Tunisia',
    'TR': 'Turkey',
    'TM': 'Turkmenistan',
    'TV': 'Tuvalu',
    'UG': 'Uganda',
    'UA': 'Ukraine',
    'AE': 'United Arab Emirates',
    'UK': 'United Kingdom',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VU': 'Vanuatu',
    'VA': 'Vatican City State',
    'VE': 'Venezuela',
    'VN': 'Viet Nam',
    'VG': 'Virgin Islands (British)',
    'VI': 'Virgin Islands (U.S.)',
    'EH': 'Western Sahara',
    'YE': 'Yemen',
    'YU': 'Yugoslavia',
    'ZR': 'Zaire',
    'ZM': 'Zambia',
    'ZW': 'Zimbabwe'}


    
    entry = entry1.get().lower()
    #messagebox.showinfo('Info', 'Enter any country to show thier COVID-19 data!')
    for en in return_countries(Country):
        try:
            if (en in entry):
            
            
                url = "https://covid-19-data.p.rapidapi.com/country"

                querystring = {"format":"undefined", "name":str(entry)}

                headers = {
                'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
                'x-rapidapi-key': "3fcc3a2353msheb9427aea7d0bf7p1a9c28jsnbd9aedc8da8c"
                }

                response = requests.request("GET", url, headers=headers, params=querystring)


            
                label1.destroy
                #print(type(response.json()))
                #print(d['name'])
                label1.config(text = "Country: " + str(response.json()[0]['country'])+
                "\nConfirmed: " + str(response.json()[0]['confirmed'])+
                "\nCritical: " + str(response.json()[0]['critical'])+
                "\nRecovered: " + str(response.json()[0]['recovered'])+             
                "\nDeaths: " + str(response.json()[0]['deaths']))

                #label1.config(text ="Country: %a \nConfirmed: %a \nCritical: %a \nRecovered: %a \nDeaths: %a" % (str(response.json()[0]['country']),str(response.json()[0]['confirmed']),str(response.json()[0]['critical']),str(response.json()[0]['recovered']),str(response.json()[0]['deaths']))               
                label1.update()
                break
        
            else:
        
                label1.destroy
                label1['text'] = "Please enter valid name of Country!"
               
                
        except:
            label1['text'] = "Something went wrong!\n Please check your connection or check that you entered a valid country."
            

def return_countries(Cont):
    for x in Cont.values():
        pass
        
    return x

 

def Convert(a): 
    pass
    
        

    
window = Tk()
window.title("COVID19 DATA")
#window.geometry("800x700")

canvas = Canvas(window,height = HEIGHT, width = WIDTH)
canvas.pack()

#photo = PhotoImage(file='/Users/solo/Documents/rsz_clark-street-mercantile-33931.gif')
#image_label = Label(window,image = photo)
#image_label.place(relwidth=1,relheight=1)

frameTitle = Frame(window, bg = '#80c1ff')
frameTitle.place(relx = 0.5,rely = 0, relwidth = 0.6, relheight=0.09, anchor='n')

label2 = Label(frameTitle, text="COVID-19 COUNTRY DATA", bg='white',fg='#80c1ff', font=('Helvetica', 25, 'bold'))
label2.place(relx=0,rely=0,relheight=1,relwidth=1)

frame = Frame(window, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely=0.1, relwidth = 0.75, relheight=0.1, anchor='n')


button1 = Button(frame, text="Get Info", activebackground="#00ff00", font = 20,command= lambda: get_news(entry1.get()))
button1.place(relx=0, rely=0, relwidth=0.25, relheight=1)

entry1 = Entry(frame, font=("Ariel", 14))
entry1.place(relx = 0.3, relwidth = 0.7, relheight= 1)
entry1.focus_set()


frame2 = Frame(window, bg ='#80c1ff', bd = 5)
frame2.place(relx=0.5,rely =0.3, relwidth = 0.75, relheight=0.6, anchor='n')


label1 = Label(frame2, font=("Ariel", 15), bg='yellow')
label1.place(relx=0,rely=0, relheight=1, relwidth=1)





window.mainloop()
