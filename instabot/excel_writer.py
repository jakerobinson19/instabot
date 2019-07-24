import xlsxwriter
import pandas as pd
import os.path
from datetime import date

def get_username_list_from_sheet(workbook):
	if os.path.isfile(workbook + '.xlsx'):
		df = pd.read_excel(workbook + '.xlsx', sheet_name=0) 
		usernames = df['Username'].tolist()
	else:
		print("File " + workbook + " does not exist")
		usernames = None

	return(usernames)

def create_workbook(container, type):
	#check type of container
	#check headers
	if type == 'today':
		todays_date = str(date.today())

		workbook = xlsxwriter.Workbook('usernames_' + todays_date + '.xlsx')
		worksheet = workbook.add_worksheet(todays_date)
	elif type == 'blacklist':
		workbook = xlsxwriter.Workbook('blacklist.xlsx')
		worksheet = workbook.add_worksheet('Blacklist')

	write_headers(workbook, worksheet)
	row = 1
	col = 0

	for username in container:
		worksheet.write(row, col, username)
		row += 1

	workbook.close()

def write_headers(workbook, worksheet, row=0):
	cell_format = workbook.add_format({'bold': True, 
									   'bg_color': 'blue', 
									   'font_color': 'white', 
									   'center_across': True, 
									   'bottom': True})

	worksheet.write(0,0, 'Username', cell_format)
	worksheet.write(0,1, 'F2F Ratio', cell_format)
	worksheet.write(0,2, "Status", cell_format)
	worksheet.set_column(0,3,30)


if __name__=="__main__":
	yesterdays_usernames = ['brixtonhamish', 'redthemini', 'gimlithegreat', 
						'finnegan_daisyduke', 'adventures_of_artie_the_dachs', 
						'dachshund_addict', 'dogsofcharmcity', 'welcometowillowsworld', 
						'thespottedachshund', 'daphne_and_dolly_dachshunds', 'mactheminiweenie', 
						'weezyarfbaby', 'mini.dachshund.penny', 'footlongfranklin', 
						'the_ombre_girls', '_donacharlie', 'jiro250417', 'queenmila___', 
						'millie_the_mini_', 'dachshundloverig', 'weenabirds', 'mochi_wells', 
						'toffeethedoxiee', 'ernie_dachshund', 'iris_ivy_violet_mini_sausages', 
						'houseofwinstor', 'dachshundmillie', 'nola_the_mini_sausage', 
						'nippy_sausagedog', 'mini_sausage_bruno', 'mochi_wells', 'dougalanddapple', 
						'patasebicosveterinaria', 'markus_sansa', 'canilgluckkautzner', 
						'bernesmexico_peraldini', 'cockapoocharly', 'lillysammymops', 
						'vetvidaoficial', 'nile_nile_crocodile', 'kristyxmiddleton', 
						'newportpetservices', 'little.koi.fish', 'mungedori', '_cherry_slimes._', 
						'zoey_susi_herkules', 'l0uil0u', 'thelittlemisskate', 'dachshund_catydogy', 
						'teckel_pippa', 'bertiedogdachsund', 'thechiwabipup', 'ipasalchicha', 
						'knopfler.the.dog', 'lucy_the_ween', 'ksothewienerdog', 'adorabledoradachs', 
						'carolinemac66', 'the_wee_sausage', 'sir_sausage', 'crisgg84', 
						'longdogrocket', 'crumpsnaturals', 'nina_sausage', 'stan_the_snag', 
						'sausagedogs_and_co', 'dachshund_amor', 'sophie_the_brew_weenie', 
						'eriksen_dachshunds', 'waylon_theweinerdog', 'lillemonator', 'noahthepickle', 
						'carsonwentzweenie', 'peanut.thedachsie', 'atxdoggo', 'bane_harvey_sausagedogs', 
						'kahlua_thewiener', 'zeldathedachshund', 'pacotheminidoxie', 'fablehavens', 
						'joey_and_nikki_the_doxie', 'cocopatascortas', 'littleweeniebutts', 
						'archweeniehutjr', 'butters_the_wiener_dog', 'gracewan.naomi','chiweeniesinbikinis', 
						'dachshundbiglove', 'leatherprince', 'dachshundloverig', 'vincent_rascal', 
						'mighty_bram', 'destinysdachs', 'dachshundolavo', 'adventures_of_ollie_the_doxie', 
						'dachshund_club_ig', 'goldieloxdox', 'dachshundlife.il', 'frankie_dachshund_uk', 
						'wienerdog.wiesje', 'mr.hazel__ms.vanilla', 'sausageofthebay', 
						'adventures_of_ollie_the_doxie', 'unrestricted_fit', 'frankandstan_', 
						'henley_the_hotdog', 'miamidachshunds', 'indie_and_gus_doxie_duo', 
						'adventures_of_lola_frida', 'mr.hazel__ms.vanilla', 'doxiemilo_', 
						'sirkingsleyofdachshundville', 'doublesausage2', 'marleysworld310', 'lnstapup', 
						'dachshund_maxmilian', 'tatusausage', 'adayinthelifeof_pablo', 'hetapreese', 
						'winston_salem_eats', 'dogs.are.greatest', 'watson_brunilda', 'dachshund_club_ig', 
						'doggy_pedia', 'zosia_dachshund', 'elsa_cream_doxie', 'boerboel_bambam', 
						'vinniethedachshund', 'cannelle_el_teckel', 'lola.the.dashchund', 'rosie_sausage', 
						'mr_boe_jangles', 'dachshund_kevin_andfriends', 'teckellucky', 'thedoxieclub', 
						'arnietheminiaturedach', 'copperthelittlesausage', 'mydachshundfamily', 'rocko_the_doxie', 
						'tina_thedachs', 'makoto.hayakawa', 'jdandpjthedachshunds', 'sosdlajamnikow', 
						'chocolateandgigi', 'sexymilanga', 'de.lune.doxie.duchess', 'dachshundsari', 
						'dachshund_ins.gram', 'puppuppluto', 'ringo_dachstarr', 'all.things.ivy', 
						'stevenwilliam69883', 'dogsalim', 'basil_doggy', 'theminidoxietwins', 
						'duracellthecopperdog', 'matakuaja', 'adventure_with_thor_pitmix', 'fotodog', 
						'its_about_the_cat', '_dalnara_', 'haileypachecolanza', 'tylerandtyketheyorkies', 
						'alicia_cavalcanti_24', 'luanmoreirafotografia', 'secretlifeof_otto', 'afraniosalsichafuracao', 
						'jessie.pelletier', 'myteenieweenie', 'chankindo', 'k9kynzi', 'picasso.biggiesmalls', 
						'heybusterbicknell', 'argos_elcan', 'mildredthesausage', 'shiung723', 
						'carioca_superminidachshund', 'dachshundclothing', 'dachshundlife.ig',
						'ronin.and.chappy.and.rily', 'wienervati', 'dachshundclothing', 'dachshund_sd', 
						'picasso.biggiesmalls', 'ralphthechocolatesausage', 'cocotheminisausage', 'magic_oreste', 
						'itshugoandwinnie', 'r0l0_thedachshund', 'eusoukoda', 'dogs_pugy', 'pepper_and_pebbles_adventures', 
						'teckelespana', 'oscarandwilma', 'tonete07', 'dachshund_catydogy', 'thepamperedpooches', 
						'leon_the_dapple', 'clintthedachshund', 'milo_mini_dachs', 'heybusterbicknell', 'dachshundloverig', 
						'_.puchi_the_dog._', 'thepamperedpooches', 'cris.doghero', 'reggie_bruin_dachshund', 
						'sidney_minisausage', 'frankie_dottie_dachshund', 'heybusterbicknell', 'honeythedoxie_', 
						'lil_dachmurphy', 'dachshundlife.ig', 'thelongbellys', 'bun_thesausagedog', 'dachshundclothing', 
						'maty197', 'mister.woof', 'scully.dachshund', 'dougie_dollie_dachshund', 'pepper_doxie_', 
						'joey_dachshund', 'oreo_thesausage', 'franklin_and_friendz', 'mrcarruthersthesausage', 
						'a_and_a_hand_made', 'scully.dachshund', 'dougie_dollie_dachshund', 'pepper_doxie_', 
						'pepper_the_dashie', 'joey_dachshund', 'ryomakawano', 'limake_dachshund', 'franklin_and_friendz', 
						'mrcarruthersthesausage', 'gusgus_the_dachshund', 'jacktheminiweenie', 'dachshund_sd', 
						'clubedachshundrn', 'nutella_salsa', 'leia_.3', 'steveandlarrygb', 'auntiejennishere',
						'we_love_dachshund_', 'dachshundbonus', 'docrandyelba', 'cutestdachshund4',
						'amoraegenesio', 'shorty_dachshund', 'nossamama', 'panchodachshund', 'gabygirllashbar', 
						'our_southern_belle', 'nighty.night.pupper', 'cccrimsonnnn', 'fluffy_kayo_okumura', 'love_sen',
						'thedaisydollops', 'dackel_anke', 'bala_dachshund', 'lexiezazzles', 'sausageriri', 'ariel_sausagedog', 
						'dachshundlove.ig', 'hotzenplotzbande', 'winston_the_wienerschnitzel', 'minimissymop', 'franklefurter', 
						'kjruthven', 'ariel_sausagedog', 'winnie_the_mini_sausagedog', 'fox_and_funny', 'twolongweenies', 
						'dachshundclub', 'ottothebratwurst', 'its_mayaandfridas_world', 'love.dachshund.for.life', 
						'oreosalsicha', 'doodlesdawg', 'dachshund_of_ig', 'thor_baby1', 'oakleyydokie', 'jazzypawzbyandrea', 
						'rosiebearthemutt', 'bddoglover', 'iammrmannanook', 'zold_korochan', 'sassy.buddy', 'fura_dachshund', 
						'adventure_doxies', 'loveryan329', 'make_y_vilmalanter', 'jericho.and.jigzie', 'pepe_peanut', 
						'zooloothedog', 'lola_bias', 'apollo.pluto_thedogs', 'ausderplatte', 'teckelchewie', 'richiesdachcam', 
						'wienerdoghotel', 'weeweenywilson', 'dachshund_love_ig', 'onecentween', 'rocket_the_dachshund', 
						'ralph_the_daxie', 'finley_boy', 'winnie_the_dash', 'beangoods', 'angelicscent', 'pawfectlybaked', 
						'milo_from_russia', 'nacozinha54', 'risenwolf18', '_alisa_photography_', 'jeankpaez', 
						'sam_the_ridgeback', '__buzzoo__19', 'elitheyorkie7', 'zevrhaska.aussies', 'ndamigou', 
						'murphyminidachshund', 'ian_dachshund', 'phileas_the_naughty_pup', 'herculesthesausage', 
						'willow.and_olive', 'gowienergo', 'wolf.the.dachshund', 'fiordiferromarina', 'apollo_1026', 
						'who_is_baxter', 'freddie_thegoldenretriever', 'goaldogs', 'ayra.the.rottie', 'luna_gsd_511', 
						'emmett_dulce', 'blaze_luu', 'animal.photographer', 'nelson_ap_benedito', 'jack.myheart.mysoul', 
						'kimmy_and_rusty', 'orel.cazares', 'lifeofapibble', 'happy.dog.training', 'apa.dog', 'grayandgim', 
						'love4wiener', 'bahia_dachshund_family', 'csigathedachshund', 'edward_and_alfred', 
						'sadiebugandstella', 'poppy_aminidachshund', 'sausagedogcentral', 'gaia_la_teckel', 
						'ullathedachshund', 'thedachshundduchess', 'thehappyhotdoghotel', 'hankandotto', 
						'pretasalchicha', 'mightymouse2016', 'ladyaubreydaxie', 'littlerubyrooo', 'shortie_the_sausage', 
						'princesse_pogo', 'sir_maximilian_the_mini', 'mollieandkokoandopi', 'imacutesausage', 
						'beaniethaweenie', 'oscar_bastille_waldron', 'sunnyandlunaa', 'the_life_of_freddo_',
						'we_love_dachshund_', 'ming.ming.love', 'charliethejewishdachshund', 'geothedachs',
						'lovedachshund_addicts', 'kloe_the_mini_doxie', 'doxiesareforlovers', 'pebbles_the_mini_dapple', 
						'our_miniature_doxie', 'toby_the.doxie', 'logan_thehotdog', 'winnie.and.zeus', 'ranger_puppr', 
						'maeby.dogface', 'fordogs.pet', 'atlasecho_duo', 'billie_hunt_lifeinpictures', 
						'kingkekoa_thenewfie', 'sheltiestyle', 'bestdachshunds', 'dosalsichasenespana', 
						'maxiesf', 'mell_dog_oficial', 'dachshundquote', 'darcy_docker', 'our_doxie_bunch', 
						'chuviscodachshund', 'lovedachshunddogs_co_clothing', 'dappledaxies', 'valy.adventures', 
						'carlinhoosdog', 'emersonthederp', 'smileymutts', 'arielesieling', 'spikey_the_white_dog', 
						'that.mutt.hazel', 'minibull.dizzy', 'rosie_littlelegs', 'hiloandkona_sausagedogs', 
						'dachshund_lunaa', 'bert_the_dachshund', 'dachshundeverywhere', 'mini_mabel', 'dittastain', 
						'doxiesandtigre', 'dulceblogueira', 'jewalshouse', 'urbanherd', 'dachshunddaily.in', 
						'bella_the_mini_sausage', 'leonconmiel', 'gigi_theminisausage', 'aspenthedoxie', 
						'adventuresofwickandmorty', 'cynthiasroyaldachshunds', 'lilys_angelxoxo', 'toshinoritheallbite', 
						'woof_shoof', 'claylrice', 'sophie.thelonghair.dachshund', 'gigi_theminisausage', 
						'lifeofbiggieandkimdogg', 'laylabellethedoxie', 'danville_dachs', 'taco.the.hotdog', 
						'littleteckel', 'brewdachs', 'hazelandmillerj', 'cookie_nenein', 'raja.of.dc', 
						'franklin_theminidach', 'finn_thepiebald', 'hayes_dachshund', 'tae_noluhime', 
						'harvey_themini_dachshund']

	create_todays_workbook(yesterdays_usernames)
	yest_names = get_username_list_from_sheet('usernames_2019-07-21.xlsx')
	print(yest_names)

