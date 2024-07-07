"#import library packages\n",
"import pandas as p\n",
"import matplotlib.pyplot as plt\n",
"import seaborn as s\n",
"import numpy as n"
]
},
{
"cell_type": "code",
"execution_count": 81,
"metadata": {},
"outputs": [],
"source": [
"import warnings\n",
"warnings.filterwarnings('ignore')"
]
},
{
"cell_type": "code",
"execution_count": 82,
32
"metadata": {},
"outputs": [],
"source": [
"# feature names\n",
"features = [\"duration\", \"protocol_type\", \"service\", \"flag\", \"src_bytes\",
\"dst_bytes\", \"land\", \"Wrong_fragment\", \"Urgent\", \"hot\",
\"num_failed_login\", \"logged_in\", \"num_compromised\", \"root_shell\",
\"su_attempted\", \"num_root\", \"num_file_creations\", \"num_shells\",
\"num_access_files\", \"num_outbound_cmds\", \"is_host_login\", \"is_guest_login\",
\"count\", \"srv_count\", \"serror_rate\", \"srv_serror_rate\", \"rerror_rate\",
\"srv_rerror_rate\", \"same_srv_rate\", \"diff_srv_rate\", \"srv_diff_host_rate\",
\"dst_host_count\", \"dst_host_srv_count\", \"dst_host_same_srv_rate\",
\"dst_host_diff_ srv_rate\", \"dst_host_same_src_port_rate\",
\"dst_host_srv_diff_host _rate\", \"dst_host_serror_rate\",
\"dst_host_srv_serror_rate\", \"dst_host_rerror_rate\",
\"dst_host_srv_rerror_rate\",\"class\"] \n",
"data = p.read_csv(\"data6.csv\", names = features)"
]
},
{
"cell_type": "code",
"execution_count": 83,
"metadata": {},
"outputs": [],
"source": [
"df=data.dropna()"
]
},
{
33
"cell_type": "code",
"execution_count": 84,
"metadata": {},
"outputs": [
{
"data": {
"text/plain": [
"array(['perl.', 'pod.', 'mscan.', 'xsnoop.', 'named.', 'guess_passwd.',\n",
" 'buffer_overflow.', 'udpstorm.', 'multihop.', 'snmpgetattack.',\n",
" 'phf.', 'worm.', 'normal.', 'warezmaster.', 'loadmodule.',\n",
" 'httptunnel.', 'sendmail.', 'apache2.', 'land.', 'saint.',\n",
" 'ftp_write.', 'teardrop.', 'sqlattack.', 'ps.', 'satan.',\n",
" 'snmpguess.', 'neptune.', 'smurf.', 'imap.', 'rootkit.',\n",
" 'portsweep.', 'ipsweep.', 'nmap.', 'processtable.', 'mailbomb.',\n",
" 'xterm.', 'xlock.', 'back.'], dtype=object)"
]
},
"execution_count": 84,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"df['class'].unique()"
]
34
},
{
"cell_type": "code",
"execution_count": 85,
"metadata": {},
"outputs": [],
"source": [
"df['attack'] = df['class'].map({'perl.':1, 'pod.':1, 'mscan.':1, 'xsnoop.':1, 'named.':1,
'guess_passwd.':1,\n",
" 'buffer_overflow.':1, 'udpstorm.':1, 'multihop.':1, 'snmpgetattack.':1,\n",
" 'phf.':1, 'worm.':1, 'normal.':0, 'warezmaster.':1, 'loadmodule.':1,\n",
" 'httptunnel.':1, 'sendmail.':1, 'apache2.':1, 'land.':1, 'saint.':1,\n",
" 'ftp_write.':1, 'teardrop.':1, 'sqlattack.':1, 'ps.':1, 'satan.':1,\n",
" 'snmpguess.':1, 'neptune.':1, 'smurf.':1, 'imap.':1, 'rootkit.':1,\n",
" 'portsweep.':1, 'ipsweep.':1, 'nmap.':1, 'processtable.':1, 'mailbomb.':1,\n",
" 'xterm.':1, 'xlock.':1, 'back.':1})"
]
},
{
"cell_type": "code",
"execution_count": 86,
"metadata": {},
"outputs": [],
"source": [
35
"df['Attack_Type'] = df['class'].map({'perl.':'Perl_Attack', 'pod.':'Pod_Attack',
'mscan.':'Mscan_Attack',\n",
"'xsnoop.':'Xsnoop_Attack','named.':'Named_Attack',
'guess_passwd.':'Guess_passwd_Attack',\n",
"'buffer_overflow.':'Buffer_overflow_Attack', 'udpstorm.':'UDPstorm_Attack',
'multihop.':'Multihop_Attack',\n",
"'snmpgetattack.':'SNMPget_Attack','phf.':'PHF_Attack', 'worm.':'Worm_Attack',
'normal.':'No_Attack_Occurs',\n",
"'warezmaster.':'Warezmaster_Attack',
'loadmodule.':'Loadmodule_Attack','httptunnel.':'HTTPtunnel_Attack', \n",
"'sendmail.':'Sendmail_Attack', 'apache2.':'Apache2_Attack', 'land.':'Land_Attack',
'saint.':'Saint_Attack',\n",
"'ftp_write.':'FTP_Write_Attack', 'teardrop.':'Teardrop_Attack',
'sqlattack.':'SQL_Attack', 'ps.':'PS_Attack',\n",
"'satan.':'Satan_Attack','snmpguess.':'SNMPguess_Attack',
'neptune.':'Neptune_Attack', 'smurf.':'Smurf_Attack',\n",
"'imap.':'IMAP_Attack','rootkit.':'Rootkit_Attack','portsweep.':'Portsweep_Attack',
'ipsweep.':'IPsweep_Attack',\n",
"'nmap.':'NMAP_Attack', 'processtable.':'Processtable_Attack',
'mailbomb.':'Mailbomb_Attack',\n",
"'xterm.':'Xterm_Attack', 'xlock.':'Xlock_Attack', 'back.':'Back_Attack'})"
]
},
{
"cell_type": "code",
"execution_count": 87,
"metadata": {},
"outputs": [
36
{
"data": {
"text/html": [
"<div>\n",
"<style scoped>\n",
" .dataframe tbody tr th:only-of-type {\n",
" vertical-align: middle;\n",
" }\n",
"\n",
" .dataframe tbody tr th {\n",
" vertical-align: top;\n",
" }\n",
"\n",
" .dataframe thead th {\n",
" text-align: right;\n",
" }\n",
"</style>\n",
"<table border=\"1\" class=\"dataframe\">\n",
" <thead>\n",
" <tr style=\"text-align: right;\">\n",
" <th></th>\n",
" <th>duration</th>\n",
" <th>protocol_type</th>\n",
" <th>service</th>\n",
" <th>flag</th>\n",
37
" <th>src_bytes</th>\n",
" <th>dst_bytes</th>\n",
" <th>land</th>\n",
" <th>Wrong_fragment</th>\n",
" <th>Urgent</th>\n",
" <th>hot</th>\n",
" <th>...</th>\n",
" <th>attack</th>\n",
" <th>Attack_Type</th>\n",
" </tr>\n",
" </thead>\n",
" <tbody>\n", "execution_count": 107,
"metadata": {},
"output_type": "execute_result"
}
],
"source": [
"df['src_bytes'].unique()"
]
},
{
"cell_type": "code",
"execution_count": 108,
"metadata": {},
"outputs": [],
38
"source": [{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": []
},
{
"cell_type": "code",
"execution_count": null,
"metadata": {},
"outputs": [],
"source": []
}
],
"metadata": {
"kernelspec": {
"display_name": "Python 3",
"language": "python",
"name": "python3"
},
"language_info": {
"codemirror_mode": {
"name": "ipython",
"version": 3
39
},
"file_extension": ".py",
"mimetype": "text/x-python",
"name": "python",
"nbconvert_exporter": "python",
"pygments_lexer": "ipython3",
"version": "3.7.4"
}
},
"nbformat": 4,
"nbformat_minor": 2
}
