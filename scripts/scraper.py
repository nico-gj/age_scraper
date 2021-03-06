from multiprocessing import Pool
import multiprocessing
import pandas as pd
from veromi_query import query

# Load in data:
ind = pd.read_csv('../data/individuals_clean.csv', low_memory=False)
ind = ind.fillna('')

# Define Pool:
pool = Pool(processes=100)

# Run query for the job:
profiles0 = pool.apply_async(query, [[0, ind, 16000, 50000]])
profiles1 = pool.apply_async(query, [[1, ind, 16000, 50000]])
profiles2 = pool.apply_async(query, [[2, ind, 16000, 50000]])
profiles3 = pool.apply_async(query, [[3, ind, 16000, 50000]])
profiles4 = pool.apply_async(query, [[4, ind, 16000, 50000]])
profiles5 = pool.apply_async(query, [[5, ind, 16000, 50000]])
profiles6 = pool.apply_async(query, [[6, ind, 16000, 50000]])
profiles7 = pool.apply_async(query, [[7, ind, 16000, 50000]])
profiles8 = pool.apply_async(query, [[8, ind, 16000, 50000]])
profiles9 = pool.apply_async(query, [[9, ind, 16000, 50000]])
profiles10 = pool.apply_async(query, [[10, ind, 16000, 50000]])
profiles11 = pool.apply_async(query, [[11, ind, 16000, 50000]])
profiles12 = pool.apply_async(query, [[12, ind, 16000, 50000]])
profiles13 = pool.apply_async(query, [[13, ind, 16000, 50000]])
profiles14 = pool.apply_async(query, [[14, ind, 16000, 50000]])
profiles15 = pool.apply_async(query, [[15, ind, 16000, 50000]])
profiles16 = pool.apply_async(query, [[16, ind, 16000, 50000]])
profiles17 = pool.apply_async(query, [[17, ind, 16000, 50000]])
profiles18 = pool.apply_async(query, [[18, ind, 16000, 50000]])
profiles19 = pool.apply_async(query, [[19, ind, 16000, 50000]])
profiles20 = pool.apply_async(query, [[20, ind, 16000, 50000]])
profiles21 = pool.apply_async(query, [[21, ind, 16000, 50000]])
profiles22 = pool.apply_async(query, [[22, ind, 16000, 50000]])
profiles23 = pool.apply_async(query, [[23, ind, 16000, 50000]])
profiles24 = pool.apply_async(query, [[24, ind, 16000, 50000]])
profiles25 = pool.apply_async(query, [[25, ind, 16000, 50000]])
profiles26 = pool.apply_async(query, [[26, ind, 16000, 50000]])
profiles27 = pool.apply_async(query, [[27, ind, 16000, 50000]])
profiles28 = pool.apply_async(query, [[28, ind, 16000, 50000]])
profiles29 = pool.apply_async(query, [[29, ind, 16000, 50000]])
profiles30 = pool.apply_async(query, [[30, ind, 16000, 50000]])
profiles31 = pool.apply_async(query, [[31, ind, 16000, 50000]])
profiles32 = pool.apply_async(query, [[32, ind, 16000, 50000]])
profiles33 = pool.apply_async(query, [[33, ind, 16000, 50000]])
profiles34 = pool.apply_async(query, [[34, ind, 16000, 50000]])
profiles35 = pool.apply_async(query, [[35, ind, 16000, 50000]])
profiles36 = pool.apply_async(query, [[36, ind, 16000, 50000]])
profiles37 = pool.apply_async(query, [[37, ind, 16000, 50000]])
profiles38 = pool.apply_async(query, [[38, ind, 16000, 50000]])
profiles39 = pool.apply_async(query, [[39, ind, 16000, 50000]])
profiles40 = pool.apply_async(query, [[40, ind, 16000, 50000]])
profiles41 = pool.apply_async(query, [[41, ind, 16000, 50000]])
profiles42 = pool.apply_async(query, [[42, ind, 16000, 50000]])
profiles43 = pool.apply_async(query, [[43, ind, 16000, 50000]])
profiles44 = pool.apply_async(query, [[44, ind, 16000, 50000]])
profiles45 = pool.apply_async(query, [[45, ind, 16000, 50000]])
profiles46 = pool.apply_async(query, [[46, ind, 16000, 50000]])
profiles47 = pool.apply_async(query, [[47, ind, 16000, 50000]])
profiles48 = pool.apply_async(query, [[48, ind, 16000, 50000]])
profiles49 = pool.apply_async(query, [[49, ind, 16000, 50000]])
profiles50 = pool.apply_async(query, [[50, ind, 16000, 50000]])
profiles51 = pool.apply_async(query, [[51, ind, 16000, 50000]])
profiles52 = pool.apply_async(query, [[52, ind, 16000, 50000]])
profiles53 = pool.apply_async(query, [[53, ind, 16000, 50000]])
profiles54 = pool.apply_async(query, [[54, ind, 16000, 50000]])
profiles55 = pool.apply_async(query, [[55, ind, 16000, 50000]])
profiles56 = pool.apply_async(query, [[56, ind, 16000, 50000]])
profiles57 = pool.apply_async(query, [[57, ind, 16000, 50000]])
profiles58 = pool.apply_async(query, [[58, ind, 16000, 50000]])
profiles59 = pool.apply_async(query, [[59, ind, 16000, 50000]])
profiles60 = pool.apply_async(query, [[60, ind, 16000, 50000]])
profiles61 = pool.apply_async(query, [[61, ind, 16000, 50000]])
profiles62 = pool.apply_async(query, [[62, ind, 16000, 50000]])
profiles63 = pool.apply_async(query, [[63, ind, 16000, 50000]])
profiles64 = pool.apply_async(query, [[64, ind, 16000, 50000]])
profiles65 = pool.apply_async(query, [[65, ind, 16000, 50000]])
profiles66 = pool.apply_async(query, [[66, ind, 16000, 50000]])
profiles67 = pool.apply_async(query, [[67, ind, 16000, 50000]])
profiles68 = pool.apply_async(query, [[68, ind, 16000, 50000]])
profiles69 = pool.apply_async(query, [[69, ind, 16000, 50000]])
profiles70 = pool.apply_async(query, [[70, ind, 16000, 50000]])
profiles71 = pool.apply_async(query, [[71, ind, 16000, 50000]])
profiles72 = pool.apply_async(query, [[72, ind, 16000, 50000]])
profiles73 = pool.apply_async(query, [[73, ind, 16000, 50000]])
profiles74 = pool.apply_async(query, [[74, ind, 16000, 50000]])
profiles75 = pool.apply_async(query, [[75, ind, 16000, 50000]])
profiles76 = pool.apply_async(query, [[76, ind, 16000, 50000]])
profiles77 = pool.apply_async(query, [[77, ind, 16000, 50000]])
profiles78 = pool.apply_async(query, [[78, ind, 16000, 50000]])
profiles79 = pool.apply_async(query, [[79, ind, 16000, 50000]])
profiles80 = pool.apply_async(query, [[80, ind, 16000, 50000]])
profiles81 = pool.apply_async(query, [[81, ind, 16000, 50000]])
profiles82 = pool.apply_async(query, [[82, ind, 16000, 50000]])
profiles83 = pool.apply_async(query, [[83, ind, 16000, 50000]])
profiles84 = pool.apply_async(query, [[84, ind, 16000, 50000]])
profiles85 = pool.apply_async(query, [[85, ind, 16000, 50000]])
profiles86 = pool.apply_async(query, [[86, ind, 16000, 50000]])
profiles87 = pool.apply_async(query, [[87, ind, 16000, 50000]])
profiles88 = pool.apply_async(query, [[88, ind, 16000, 50000]])
profiles89 = pool.apply_async(query, [[89, ind, 16000, 50000]])
profiles90 = pool.apply_async(query, [[90, ind, 16000, 50000]])
profiles91 = pool.apply_async(query, [[91, ind, 16000, 50000]])
profiles92 = pool.apply_async(query, [[92, ind, 16000, 50000]])
profiles93 = pool.apply_async(query, [[93, ind, 16000, 50000]])
profiles94 = pool.apply_async(query, [[94, ind, 16000, 50000]])
profiles95 = pool.apply_async(query, [[95, ind, 16000, 50000]])
profiles96 = pool.apply_async(query, [[96, ind, 16000, 50000]])
profiles97 = pool.apply_async(query, [[97, ind, 16000, 50000]])
profiles98 = pool.apply_async(query, [[98, ind, 16000, 50000]])
profiles99 = pool.apply_async(query, [[99, ind, 16000, 50000]])
profiles0 = profiles0.get()
profiles1 = profiles1.get()
profiles2 = profiles2.get()
profiles3 = profiles3.get()
profiles4 = profiles4.get()
profiles5 = profiles5.get()
profiles6 = profiles6.get()
profiles7 = profiles7.get()
profiles8 = profiles8.get()
profiles9 = profiles9.get()
profiles10 = profiles10.get()
profiles11 = profiles11.get()
profiles12 = profiles12.get()
profiles13 = profiles13.get()
profiles14 = profiles14.get()
profiles15 = profiles15.get()
profiles16 = profiles16.get()
profiles17 = profiles17.get()
profiles18 = profiles18.get()
profiles19 = profiles19.get()
profiles20 = profiles20.get()
profiles21 = profiles21.get()
profiles22 = profiles22.get()
profiles23 = profiles23.get()
profiles24 = profiles24.get()
profiles25 = profiles25.get()
profiles26 = profiles26.get()
profiles27 = profiles27.get()
profiles28 = profiles28.get()
profiles29 = profiles29.get()
profiles30 = profiles30.get()
profiles31 = profiles31.get()
profiles32 = profiles32.get()
profiles33 = profiles33.get()
profiles34 = profiles34.get()
profiles35 = profiles35.get()
profiles36 = profiles36.get()
profiles37 = profiles37.get()
profiles38 = profiles38.get()
profiles39 = profiles39.get()
profiles40 = profiles40.get()
profiles41 = profiles41.get()
profiles42 = profiles42.get()
profiles43 = profiles43.get()
profiles44 = profiles44.get()
profiles45 = profiles45.get()
profiles46 = profiles46.get()
profiles47 = profiles47.get()
profiles48 = profiles48.get()
profiles49 = profiles49.get()
profiles50 = profiles50.get()
profiles51 = profiles51.get()
profiles52 = profiles52.get()
profiles53 = profiles53.get()
profiles54 = profiles54.get()
profiles55 = profiles55.get()
profiles56 = profiles56.get()
profiles57 = profiles57.get()
profiles58 = profiles58.get()
profiles59 = profiles59.get()
profiles60 = profiles60.get()
profiles61 = profiles61.get()
profiles62 = profiles62.get()
profiles63 = profiles63.get()
profiles64 = profiles64.get()
profiles65 = profiles65.get()
profiles66 = profiles66.get()
profiles67 = profiles67.get()
profiles68 = profiles68.get()
profiles69 = profiles69.get()
profiles70 = profiles70.get()
profiles71 = profiles71.get()
profiles72 = profiles72.get()
profiles73 = profiles73.get()
profiles74 = profiles74.get()
profiles75 = profiles75.get()
profiles76 = profiles76.get()
profiles77 = profiles77.get()
profiles78 = profiles78.get()
profiles79 = profiles79.get()
profiles80 = profiles80.get()
profiles81 = profiles81.get()
profiles82 = profiles82.get()
profiles83 = profiles83.get()
profiles84 = profiles84.get()
profiles85 = profiles85.get()
profiles86 = profiles86.get()
profiles87 = profiles87.get()
profiles88 = profiles88.get()
profiles89 = profiles89.get()
profiles90 = profiles90.get()
profiles91 = profiles91.get()
profiles92 = profiles92.get()
profiles93 = profiles93.get()
profiles94 = profiles94.get()
profiles95 = profiles95.get()
profiles96 = profiles96.get()
profiles97 = profiles97.get()
profiles98 = profiles98.get()
profiles99 = profiles99.get()

# Combine Frames:
frames=[]
frames.extend([profiles0, profiles1, profiles2, profiles3, profiles4, profiles5, profiles6, profiles7, profiles8, profiles9])
frames.extend([profiles10, profiles11, profiles12, profiles13, profiles14, profiles15, profiles16, profiles17, profiles18, profiles19])
frames.extend([profiles20, profiles21, profiles22, profiles23, profiles24, profiles25, profiles26, profiles27, profiles28, profiles29])
frames.extend([profiles30, profiles31, profiles32, profiles33, profiles34, profiles35, profiles36, profiles37, profiles38, profiles39])
frames.extend([profiles40, profiles41, profiles42, profiles43, profiles44, profiles45, profiles46, profiles47, profiles48, profiles49])
frames.extend([profiles50, profiles51, profiles52, profiles53, profiles54, profiles55, profiles56, profiles57, profiles58, profiles59])
frames.extend([profiles60, profiles61, profiles62, profiles63, profiles64, profiles65, profiles66, profiles67, profiles68, profiles69])
frames.extend([profiles70, profiles71, profiles72, profiles73, profiles74, profiles75, profiles76, profiles77, profiles78, profiles79])
frames.extend([profiles80, profiles81, profiles82, profiles83, profiles84, profiles85, profiles86, profiles87, profiles88, profiles89])
frames.extend([profiles90, profiles91, profiles92, profiles93, profiles94, profiles95, profiles96, profiles97, profiles98, profiles99])

profiles = pd.concat(frames).reset_index(drop=True)

profiles = profiles.drop_duplicates().reset_index(drop=True)

# Export results as CSV
profiles.to_csv('../output/scraper_output/individuals_clean_ages.csv', index=False)
