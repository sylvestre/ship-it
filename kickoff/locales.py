# coding: utf-8

languages = {
    'af': {'English': 'Afrikaans', 'native': 'Afrikaans'},
    'ach': {'English': 'Acholi',                    'native': 'Acholi'},
    'ak': {'English': 'Akan',                      'native': 'Akan'},  # unverified native name
    'am-et': {'English': 'Amharic',                   'native': u'አማርኛ'},
    'an': {'English': 'Aragonese',                 'native': 'aragonés'},
    'ar': {'English': 'Arabic',                    'native': 'عربي'},
    'as': {'English': 'Assamese',                  'native': 'অসমীয়া'},
    'ast': {'English': 'Asturian',                  'native': 'Asturianu'},
    'az': {'English': 'Azerbaijani',               'native': 'Azərbaycanca'},
    'be': {'English': 'Belarusian',                'native': 'Беларуская'},
    'bg': {'English': 'Bulgarian',                 'native': 'Български'},
    'bn-BD': {'English': 'Bengali (Bangladesh)',      'native': 'বাংলা (বাংলাদেশ)'},
    'bn-IN': {'English': 'Bengali (India)',           'native': 'বাংলা (ভারত)'},
    'br': {'English': 'Breton',                    'native': 'Brezhoneg'},
    'bs': {'English': 'Bosnian',                   'native': 'Bosanski'},
    'ca': {'English': 'Catalan',                   'native': 'Català'},
    'ca-valencia': {'English': 'Catalan (Valencian)',       'native': 'català (valencià)'},  # not iso-639-1. a=l10n-drivers
    'cs': {'English': 'Czech',                     'native': 'Čeština'},
    'csb': {'English': 'Kashubian',                 'native': 'Kaszëbsczi'},
    'cy': {'English': 'Welsh',                     'native': 'Cymraeg'},
    'da': {'English': 'Danish',                    'native': 'Dansk'},
    'dbg': {'English': 'Debug Robot',               'native': 'Ḓḗƀŭɠ Řǿƀǿŧ'},  # Used for site debugging
    'de': {'English': 'German',                    'native': 'Deutsch'},
    'de-AT': {'English': 'German (Austria)',          'native': 'Deutsch (Österreich)'},
    'de-CH': {'English': 'German (Switzerland)',      'native': 'Deutsch (Schweiz)'},
    'de-DE': {'English': 'German (Germany)',          'native': 'Deutsch (Deutschland)'},
    'dsb': {'English': 'Lower Sorbian',             'native': 'Dolnoserbšćina'},  # iso-639-2
    'el': {'English': 'Greek',                     'native': 'Ελληνικά'},
    'en-AU': {'English': 'English (Australian)',      'native': 'English (Australian)'},
    'en-CA': {'English': 'English (Canadian)',        'native': 'English (Canadian)'},
    'en-GB': {'English': 'English (British)',         'native': 'English (British)'},
    'en-NZ': {'English': 'English (New Zealand)',     'native': 'English (New Zealand)'},
    'en-US': {'English': 'English (US)',              'native': 'English (US)'},
    'en-ZA': {'English': 'English (South African)',   'native': 'English (South African)'},
    'eo': {'English': 'Esperanto',                 'native': 'Esperanto'},
    'es': {'English': 'Spanish',                   'native': 'Español'},
    'es-AR': {'English': 'Spanish (Argentina)',       'native': 'Español (de Argentina)'},
    'es-CL': {'English': 'Spanish (Chile)',           'native': 'Español (de Chile)'},
    'es-ES': {'English': 'Spanish (Spain)',           'native': 'Español (de España)'},
    'es-MX': {'English': 'Spanish (Mexico)',          'native': 'Español (de México)'},
    'et': {'English': 'Estonian',                  'native': 'Eesti keel'},
    'eu': {'English': 'Basque',                    'native': 'Euskara'},
    'fa': {'English': 'Persian',                   'native': 'فارسی'},
    'ff': {'English': 'Fulah',                     'native': 'Pulaar-Fulfulde'},
    'fi': {'English': 'Finnish',                   'native': 'suomi'},
    'fj-FJ': {'English': 'Fijian',                    'native': 'Vosa vaka-Viti'},
    'fr': {'English': 'French',                    'native': 'Français'},
    'fur-IT': {'English': 'Friulian',                  'native': 'Furlan'},
    'fy-NL': {'English': 'Frisian',                   'native': 'Frysk'},
    'ga': {'English': 'Irish',                     'native': 'Gaeilge'},
    'ga-IE': {'English': 'Irish',                     'native': 'Gaeilge'},
    'gd': {'English': 'Gaelic (Scotland)',         'native': 'Gàidhlig'},
    'gl': {'English': 'Galician',                  'native': 'Galego'},
    'gu': {'English': 'Gujarati',                  'native': 'ગુજરાતી'},
    'gu-IN': {'English': 'Gujarati (India)',          'native': 'ગુજરાતી (ભારત)'},
    'he': {'English': 'Hebrew',                    'native': 'עברית'},
    'hi': {'English': 'Hindi',                     'native': 'हिन्दी'},
    'hi-IN': {'English': 'Hindi (India)',             'native': 'हिन्दी (भारत)'},
    'hr': {'English': 'Croatian',                  'native': 'Hrvatski'},
    'hsb': {'English': 'Upper Sorbian',             'native': 'Hornjoserbsce'},
    'hu': {'English': 'Hungarian',                 'native': 'magyar'},
    'hy-AM': {'English': 'Armenian',                  'native': 'Հայերեն'},
    'id': {'English': 'Indonesian',                'native': 'Bahasa Indonesia'},
    'is': {'English': 'Icelandic',                 'native': 'íslenska'},
    'it': {'English': 'Italian',                   'native': 'Italiano'},
    'ja': {'English': 'Japanese',                  'native': '日本語'},
    'ja-JP-mac': {'English': 'Japanese',                  'native': '日本語'},  # not iso-639-1
    'ka': {'English': 'Georgian',                  'native': 'ქართული'},
    'kk': {'English': 'Kazakh',                    'native': 'Қазақ'},
    'km': {'English': 'Khmer',                     'native': 'ខ្មែរ'},
    'kn': {'English': 'Kannada',                   'native': 'ಕನ್ನಡ'},
    'ko': {'English': 'Korean',                    'native': '한국어'},
    'ku': {'English': 'Kurdish',                   'native': 'Kurdî'},
    'la': {'English': 'Latin',                     'native': 'Latina'},
    'lg': {'English': 'Luganda',                   'native': 'Luganda'},
    'lij': {'English': 'Ligurian',                  'native': 'Ligure'},
    'lo': {'English': 'Lao',                       'native': 'ພາສາລາວ'},
    'lt': {'English': 'Lithuanian',                'native': 'lietuvių kalba'},
    'lv': {'English': 'Latvian',                   'native': 'Latviešu'},
    'mai': {'English': 'Maithili',                  'native': 'मैथिली মৈথিলী'},
    'mg': {'English': 'Malagasy',                  'native': 'Malagasy'},
    'mi': {'English': 'Maori (Aotearoa)',          'native': 'Māori (Aotearoa)'},
    'mk': {'English': 'Macedonian',                'native': 'Македонски'},
    'ml': {'English': 'Malayalam',                 'native': 'മലയാളം'},
    'mn': {'English': 'Mongolian',                 'native': 'Монгол'},
    'mr': {'English': 'Marathi',                   'native': 'मराठी'},
    'ms': {'English': 'Malay',                     'native': 'Melayu'},
    'my': {'English': 'Burmese',                   'native': 'မြန်မာဘာသာ'},
    'nb-NO': {'English': 'Norwegian (Bokmål)',        'native': 'Norsk bokmål'},
    'ne-NP': {'English': 'Nepali',                    'native': 'नेपाली'},
    'nn-NO': {'English': 'Norwegian (Nynorsk)',       'native': 'Norsk nynorsk'},
    'nl': {'English': 'Dutch',                     'native': 'Nederlands'},
    'nr': {'English': 'Ndebele, South',            'native': 'isiNdebele'},
    'nso': {'English': 'Northern Sotho',            'native': 'Sepedi'},
    'oc': {'English': 'Occitan (Lengadocian)',     'native': 'occitan (lengadocian)'},
    'or': {'English': 'Oriya',                     'native': 'ଓଡ଼ିଆ'},
    'pa': {'English': 'Punjabi',                   'native': 'ਪੰਜਾਬੀ'},
    'pa-IN': {'English': 'Punjabi (India)',           'native': 'ਪੰਜਾਬੀ (ਭਾਰਤ)'},
    'pl': {'English': 'Polish',                    'native': 'Polski'},
    'pt-BR': {'English': 'Portuguese (Brazilian)',    'native': 'Português (do Brasil)'},
    'pt-PT': {'English': 'Portuguese (Portugal)',     'native': 'Português (Europeu)'},
    'ro': {'English': 'Romanian',                  'native': 'română'},
    'rm': {'English': 'Romansh',                   'native': 'rumantsch'},
    'ru': {'English': 'Russian',                   'native': 'Русский'},
    'rw': {'English': 'Kinyarwanda',               'native': 'Ikinyarwanda'},
    'sa': {'English': 'Sanskrit',                  'native': 'संस्कृत'},
    'sah': {'English': 'Sakha',                     'native': 'Сахалыы'},
    'si': {'English': 'Sinhala',                   'native': 'සිංහල'},
    'sk': {'English': 'Slovak',                    'native': 'slovenčina'},
    'sl': {'English': 'Slovenian',                 'native': 'Slovenščina'},
    'son': {'English': 'Songhai',                   'native': 'Soŋay'},
    'sq': {'English': 'Albanian',                  'native': 'Shqip'},
    'sr': {'English': 'Serbian',                   'native': 'Српски'},
    'sr-Cyrl': {'English': 'Serbian',                   'native': 'Српски'},  # follows RFC 4646
    'sr-Latn': {'English': 'Serbian',                   'native': 'Srpski'},  # follows RFC 4646
    'ss': {'English': 'Siswati',                   'native': 'siSwati'},
    'st': {'English': 'Southern Sotho',            'native': 'Sesotho'},
    'sv-SE': {'English': 'Swedish',                   'native': 'Svenska'},
    'sw': {'English': 'Swahili',                   'native': 'Kiswahili'},
    'ta': {'English': 'Tamil',                     'native': 'தமிழ்'},
    'ta-IN': {'English': 'Tamil (India)',             'native': 'தமிழ் (இந்தியா)'},
    'ta-LK': {'English': 'Tamil (Sri Lanka)',         'native': 'தமிழ் (இலங்கை)'},
    'te': {'English': 'Telugu',                    'native': 'తెలుగు'},
    'th': {'English': 'Thai',                      'native': 'ไทย'},
    'tn': {'English': 'Tswana',                    'native': 'Setswana'},
    'tr': {'English': 'Turkish',                   'native': 'Türkçe'},
    'ts': {'English': 'Tsonga',                    'native': 'Xitsonga'},
    'tt-RU': {'English': 'Tatar',                     'native': 'Tatarça'},
    'uk': {'English': 'Ukrainian',                 'native': 'Українська'},
    'ur': {'English': 'Urdu',                      'native': 'اُردو'},
    'uz': {'English': 'Uzbek',                     'native': 'Oʻzbek tili'},
    've': {'English': 'Venda',                     'native': 'Tshivenḓa'},
    'vi': {'English': 'Vietnamese',                'native': 'Tiếng Việt'},
    'wo': {'English': 'Wolof',                     'native': 'Wolof'},
    'x-testing': {'English': 'Testing',                   'native': 'Ŧḗşŧīƞɠ'},
    'xh': {'English': 'Xhosa',                     'native': 'isiXhosa'},
    'zh-CN': {'English': 'Chinese (Simplified)',      'native': '中文 (简体)'},
    'zh-TW': {'English': 'Chinese (Traditional)',     'native': '正體中文 (繁體)'},
    'zu': {'English': 'Zulu',                      'native': 'isiZulu'}
}