colors_QC7 = [
    [128,128,128],     #ART_NORM: white
    [255,99,71],     #ART_FOLD: orange
    [0,255,0],   #ART_DARKSPOT: green
    [255,0,0],   #ART_PEN: red
    [255,0,255],   #ART_EDGE: pink
    [75,0,130],      # FOCUS: violet
    [255,255,255]   #BACK
]


colors_COADREAD = [[50,50,250], #TUMOR, ADENOM_HG: blue
          [50,250,50], #MUC, ADENOM_LG: green
          [255,165,0], #TU_STROMA: orange
          [128,128,128],  #SUBMUC: gray
          [232,91,81], #MUSC_PROP, MUSC_MUC: dark salmon
          [128,128,128], #ADVENT, VESSEL: gray
          [255,20,147], #LYMPH_NODE, LYMPH_TIS, LYM_AGGR: pink
          [212, 175, 55], #ULCUS, NECROSIS: gold
          [128,128,128], #BLOOD: gray
          [245, 66, 66], #MUCIN: red
          [255,255,255]] #BACK: white   

colors_LUNG = [
    [0, 0, 255],
    #[255, 0, 0],
    [255, 165, 0],
    [0, 0, 128],
    [0, 255, 0],
    [128, 0, 128],
    [128, 128, 0],
    [255, 192, 203],
    [192, 192, 192],
    [128, 0, 0],
    [0, 255, 255],
    [255, 255, 0],
    [255, 255, 255]
]

'''
    Blue: [0, 0, 255] TUMOR
    Orange: [255, 165, 0] TUMOR STROMA
    Navy Blue: [0, 0, 128] NECROSIS
    Green: [0, 255, 0] MUCIN
    Purple: [128, 0, 128] BENIGN LUNG
    Olive: [128, 128, 0] STROMA, NERVE, FAT, MUSCLE, VESSEL
    Pink: [255, 192, 203] BLOOD
    Light Gray: [192, 192, 192] BRONCHUS
    Maroon: [128, 0, 0] CARTILAGE
    Aqua: [0, 255, 255] GLAND_BRONCH
    Yellow: [255, 255, 0] LYMPH_AGGR, LYMPH_NODE
    White: [255,255,255] BACK
'''

colors_LN_COLON = [[50,50,250],     # TUMOR: blue
                   [255,165,0],     # STROMA: orange
                   [50,250,50],     # LYMPH_NODE: green
                   [255,223,186],       # PERILYMPH: gold (light yellow for better visibility)
                   [255,192,203],   # NECROSIS: pink
                   [255,0,0],   # BLOOD: red
                   [139,69,19],     # MUCIN: brown
                   [128,128,128]]   # BACK: gray


#Artifact detection model
colors_ART = [[128,128,128], #NORM:GRAY
          [255,165,0], #DARK_SPOT: ORANGE
          [250,50,50], #FOLD: RED
          [50,250,50], #FOREIGN: GREEN
          [212, 175, 55], #PEN: GOLD
          [255,20,147], #EDGE: PINK
          [232,91,81], #AIR: DARK SALMON
          [50,50,250]] #FOCUS: BLUE

#RCC (old version)
colors_RCC = [ [50, 50, 250], #TUMOR: Blau # Will work only in "tumor" masks, in "subtyping" masks will be re-classified in 11-13
                      [255, 255, 255],  # TUMOR_REGRESS: white
                      [255, 255, 255],  # NECROSIS: white
                      [255, 255, 255],  # KIDNEY_BENIGN: white
                      [255, 255, 255],  # UROTHEL: white
                      [255, 255, 255],  # FAT: white
                      [255, 255, 255],  # STROMA: white
                      [255, 255, 255],  # BLOOD: white
                      [255, 255, 255], # ADRENAL: white
                      [128, 128, 128], # BACK: gray
                      [50, 50, 250],  # CCRCC: blue
                      [50, 250, 50],  # PRCC: green
                      [250, 50, 50]]  # CHRCC: red





colors_rcc_subtype = [[50, 50, 250],  # CCRCC: blue
                      [50, 250, 50],  # PRCC: green
                      [250, 50, 50],  # CHRRCC: red
                      [212, 175, 55],  # TUMOR_REGRESS: gold
                      [255, 20, 147],  # NECROSIS: pink
                      [255, 165, 0],  # KIDNEY_BENIGN: orange
                      [255, 165, 0],  # KIDNEY_BENIGN_ATROPH: orange
                      [128, 128, 128],  # FAT: gray
                      [128, 128, 128],  # STROMA: gray
                      [128, 128, 128],  # BLOOD: gray
                      [128, 128, 128], # ADRENAL: gray
                      [255, 255, 255]]  #BACK: white


colors_rcc_tu = [[50, 50, 250],  # CCRCC: blue
                 [50, 50, 250],  # PRCC: blue
                 [50, 50, 250],  # CHRRCC: blue
                 [212, 175, 55],  # TUMOR_REGRESS: gold
                 [255, 20, 147],  # NECROSIS: pink
                 [255, 165, 0],  # KIDNEY_BENIGN: orange
                 [255, 165, 0],  # KIDNEY_BENIGN_ATROPH: orange
                 [128, 128, 128],  # FAT: gray
                 [128, 128, 128],  # STROMA: gray
                 [128, 128, 128],  # BLOOD: gray
                 [128, 128, 128],  # ADRENAL: gray
                 [255, 255, 255]]  # BACK: white

colors_rcc_tu_red = [[50, 50, 250],  # CCRCC: blue
                 [50, 50, 250],  # PRCC: blue
                 [50, 50, 250],  # CHRRCC: blue
                 [255, 255, 255],  # TUMOR_REGRESS: gold
                 [255, 255, 255],  # NECROSIS: pink
                 [255, 255, 255],  # KIDNEY_BENIGN: orange
                 [255, 255, 255],  # KIDNEY_BENIGN_ATROPH: orange
                 [255, 255, 255],  # FAT: gray
                 [255, 255, 255],  # STROMA: gray
                 [255, 255, 255],  # BLOOD: gray
                 [255, 255, 255],  # ADRENAL: gray
                 [255, 255, 255]]  # BACK: white
