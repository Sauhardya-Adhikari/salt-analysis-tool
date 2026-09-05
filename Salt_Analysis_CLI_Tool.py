# ==========================================
# Author: Sauhardya Adhikari
# Project: Salt Analysis CLI Tool
# Copyright (c) 2026. All rights reserved.
# This code is view-only and may not be 
# copied or redistributed without permission.
# ==========================================
# INORGANIC SALT ANALYSIS SIMULATOR
import time

print('WELCOME TO THE INORGANIC SALT ANALYSIS SIMULATOR\n')
time.sleep(1)

while True:
    print('\nPLEASE SELECT YOUR DESIRED WAY TO PROCEED:')
    print('1. CATION PRELIMINARY ANALYSIS')
    print('2. ANION PRELIMINARY ANALYSIS')
    print('3. CATION CONFIRMATORY ANALYSIS')
    print('4. ANION CONFIRMATORY ANALYSIS')
    print('5. EXIT')
    
    time.sleep(1)
    try:
        choice_1 = int(input('Enter your option number: '))
    except ValueError:
        print('Please enter a valid integer number.')
        continue
    
    time.sleep(1)
    
    # ---------------------------------------------------------
    # 1. CATION PRELIMINARY ANALYSIS
    # ---------------------------------------------------------
    if choice_1 == 1:
        while True:
            print('\nPLEASE SELECT THE CORRECT APPEARANCE OF YOUR SALT:')
            print('1. WHITE')
            print('2. NON-WHITE')
            print('3. EXIT TO MAIN MENU')
            
            time.sleep(1)
            choice_2 = int(input('Enter the choice number: '))
            time.sleep(1)
            
            if choice_2 == 1:
                print('\nBORAX BEAD TEST IS NOT NEEDED')
                time.sleep(1)
                
                while True:
                    print('\nPLEASE SELECT THE WAY YOU WANT TO PROCEED:')
                    print('1. DRY HEATING TEST')
                    print('2. FLAME TEST')
                    print('3. GROUP ANALYSIS')
                    print('4. EXIT TO PREVIOUS MENU')
                    
                    time.sleep(1)
                    choice_3 = int(input('Enter the choice number: '))
                    time.sleep(1)
                    
                    if choice_3 == 1:
                        while True:
                            print('\nSELECT YOUR OBSERVATION CORRECTLY:')
                            print('1. White Sublimate Formed')
                            print('2. Blue when cold and white when hot')
                            print('3. White when cold and yellow when hot')
                            print('4. Yellow when cold and brown when hot')
                            print('5. Coloured Salt turned to brown/blue on heating')
                            print('6. Decripitation with brown fumes')
                            print('7. Yellow when hot')
                            print('8. Dirty yellow or yellow when hot')
                            print('9. Reverting to previous menu')
                            print('10. Exit Dry Heating Test')
                            
                            choice_4 = int(input('Enter the choice number: '))
                            time.sleep(1)
                            
                            if choice_4 == 1:
                                print('May be Ammonium Cation')
                            elif choice_4 == 2:
                                print('May be Copper Cation')
                            elif choice_4 == 3:
                                print('May be Zinc Cation')
                            elif choice_4 == 4:
                                print('May be Lead Cation')
                            elif choice_4 == 5:
                                print('May be Cobalt, Copper or Manganese Cation')
                            elif choice_4 == 6:
                                print('May be Lead Nitrate Salt')
                            elif choice_4 == 7:
                                print('May be Nickel Salt')
                            elif choice_4 == 8:
                                print('May be Iron Salt')
                            elif choice_4 == 9:
                                break
                            elif choice_4 == 10:
                                break
                            else:
                                print('Input Valid Option')
                                
                    elif choice_3 == 2:
                        while True:
                            print('\nSELECT YOUR OBSERVATION CORRECTLY:')
                            print('1. Transient Brick Red Flame')
                            print('2. Persistent Crimson Red Flame')
                            print('3. Apple Green Flame')
                            print('4. Bluish Green Flame')
                            print('5. Lambent Blue Flame')
                            print('6. Green Flashes')
                            print('7. Reverting to previous menu')
                            print('8. Exit Flame Test')
                            
                            time.sleep(1)
                            choice_5 = int(input('Enter the choice number: '))
                            time.sleep(1)
                            
                            if choice_5 == 1:
                                print('May be Calcium Cation')
                            elif choice_5 == 2:
                                print('May be Strontium Cation')
                            elif choice_5 == 3:
                                print('May be Barium Cation')
                            elif choice_5 == 4:
                                print('May be Copper Cation')
                            elif choice_5 == 5:
                                print('May be Lead Cation')
                            elif choice_5 == 6:
                                print('May be Manganese Cation')
                            elif choice_5 == 7:
                                break
                            elif choice_5 == 8:
                                break
                            else:
                                print('Input Valid Option')
                                
                    elif choice_3 == 3:
                        print('\nIN GROUP ANALYSIS WE TEST WITH DIFFERENT REAGENTS SEQUENCE WISE.')
                        time.sleep(1)
                        print('Small amount of salt was taken and 1-2ml of Sodium Hydroxide solution was added and heated. Did you notice smell of Ammonia? Did it give white fumes with dil. HCl?')
                        a_in = input('YES/NO: ')
                        
                        if a_in.lower() == 'yes':
                            print('GROUP ZERO PRESENT')
                            time.sleep(1)
                            print('The gas evolved on passing through Nessler Reagent gives brown precipitate.')
                            time.sleep(1)
                            print('Congratulations, you got Ammonia as your cation!')
                        else:
                            print('Then, Dilute Hydrochloric Acid was added. Did you see any type of white ppt.?')
                            b_in = input('YES/NO: ')
                            if b_in.lower() == 'yes':
                                print('GROUP ONE PRESENT. Group One contains Lead.')
                            else:
                                print('Then, we pass hydrogen sulphide gas through it. Did it form any kind of Black/yellow Ppt.?')
                                c_in = input('YES/NO: ')
                                if c_in.lower() == 'yes':
                                    print('GROUP TWO PRESENT. Group Two contains Lead, Copper and Arsenic.')
                                else:
                                    print('Then we take Original Solution, add conc. Nitric Acid, boil, add solid Ammonium Chloride and Ammonium Hydroxide. Did you notice brown or green/white gelatinous ppt.?')
                                    d_in = input('YES/NO: ')
                                    if d_in.lower() == 'yes':
                                        print('GROUP THREE PRESENT. Group Three contains Iron and Aluminium.')
                                    else:
                                        print('Then we pass Hydrogen Sulphide Gas through it. Do you notice white/flesh colored or black ppt.?')
                                        e_in = input('YES/NO: ')
                                        if e_in.lower() == 'yes':
                                            print('GROUP FOUR PRESENT. Group Four contains Nickel, Cobalt, Zinc and Manganese.')
                                        else:
                                            print('Then we take Original Solution, add solid Ammonium Chloride, Ammonium Hydroxide and Ammonium Carbonate. Do you notice white ppt.?')
                                            f_in = input('YES/NO: ')
                                            if f_in.lower() == 'yes':
                                                print('GROUP FIVE PRESENT. Group Five contains Barium, Strontium and Calcium.')
                                            else:
                                                print('Then we add Disodium Hydrogen Orthophosphate solution. Do you notice white ppt.?')
                                                g_in = input('YES/NO: ')
                                                if g_in.lower() == 'yes':
                                                    print('GROUP SIX PRESENT. Group Six contains Magnesium.')
                                                else:
                                                    print('Unknown Cation.')
                    elif choice_3 == 4:
                        break        
            elif choice_2 == 2:
                print('\nNon-White Salts need to be tested with Borax bead test.')
                print('CHOOSE BEAD COLOUR OBSERVATION:')
                print('1. Blue (cold) / green (hot) oxidising, Red opaque(cold) / colourless(hot) reducing')
                print('2. Yellow (cold) / yellowish brown (hot) oxidising, green (cold/hot) reducing')
                print('3. Light violet (cold/hot) oxidising, colourless (cold/hot) reducing')
                print('4. Deep blue in both oxidising and reducing flame')
                print('5. Brown bead in oxidising flame and grey bead in reducing flame')
                print('6. Reverting to previous menu')
                print('7. Exit Borax bead test')
                
                bead_choice = int(input('Enter the choice number: '))
                if bead_choice == 1:
                    print('It may be copper cation')
                elif bead_choice == 2:
                    print('It may be iron cation')
                elif bead_choice == 3:
                    print('It may be manganese cation')
                elif bead_choice == 4:
                    print('It may be cobalt cation')
                elif bead_choice == 5:
                    print('It may be nickel cation')
                elif bead_choice == 6:
                    break
                elif bead_choice == 7:
                    break

                while True:
                    print('\nPLEASE SELECT THE WAY YOU WANT TO PROCEED:')
                    print('1. DRY HEATING TEST')
                    print('2. FLAME TEST')
                    print('3. GROUP ANALYSIS')
                    print('4. EXIT TO PREVIOUS MENU')
                    
                    time.sleep(1)
                    choice_3 = int(input('Enter the choice number: '))
                    time.sleep(1)
                    
                    if choice_3 == 1:
                        while True:
                            print('\nSELECT YOUR OBSERVATION CORRECTLY:')
                            print('1. White Sublimate Formed')
                            print('2. Blue when cold and white when hot')
                            print('3. White when cold and yellow when hot')
                            print('4. Yellow when cold and brown when hot')
                            print('5. Coloured Salt turned to brown/blue on heating')
                            print('6. Decripitation with brown fumes')
                            print('7. Yellow when hot')
                            print('8. Dirty yellow or yellow when hot')
                            print('9. Reverting to previous menu')
                            print('10. Exit Dry Heating Test')
                            
                            choice_4 = int(input('Enter the choice number: '))
                            time.sleep(1)
                            
                            if choice_4 == 1:
                                print('May be Ammonium Cation')
                            elif choice_4 == 2:
                                print('May be Copper Cation')
                            elif choice_4 == 3:
                                print('May be Zinc Cation')
                            elif choice_4 == 4:
                                print('May be Lead Cation')
                            elif choice_4 == 5:
                                print('May be Cobalt, Copper or Manganese Cation')
                            elif choice_4 == 6:
                                print('May be Lead Nitrate Salt')
                            elif choice_4 == 7:
                                print('May be Nickel Salt')
                            elif choice_4 == 8:
                                print('May be Iron Salt')
                            elif choice_4 == 9:
                                break
                            elif choice_4 == 10:
                                break
                            else:
                                print('Input Valid Option')
                                
                    elif choice_3 == 2:
                        while True:
                            print('\nSELECT YOUR OBSERVATION CORRECTLY:')
                            print('1. Transient Brick Red Flame')
                            print('2. Persistent Crimson Red Flame')
                            print('3. Apple Green Flame')
                            print('4. Bluish Green Flame')
                            print('5. Lambent Blue Flame')
                            print('6. Green Flashes')
                            print('7. Reverting to previous menu')
                            print('8. Exit Flame Test')
                            
                            time.sleep(1)
                            choice_5 = int(input('Enter the choice number: '))
                            time.sleep(1)
                            
                            if choice_5 == 1:
                                print('May be Calcium Cation')
                            elif choice_5 == 2:
                                print('May be Strontium Cation')
                            elif choice_5 == 3:
                                print('May be Barium Cation')
                            elif choice_5 == 4:
                                print('May be Copper Cation')
                            elif choice_5 == 5:
                                print('May be Lead Cation')
                            elif choice_5 == 6:
                                print('May be Manganese Cation')
                            elif choice_5 == 7:
                                break
                            elif choice_5 == 8:
                                break
                            else:
                                print('Input Valid Option')
                                
                    elif choice_3 == 3:
                        print('\nIN GROUP ANALYSIS WE TEST WITH DIFFERENT REAGENTS SEQUENCE WISE.')
                        time.sleep(1)
                        print('Small amount of salt was taken and 1-2ml of Sodium Hydroxide solution was added and heated. Did you notice smell of Ammonia? Did it give white fumes with dil. HCl?')
                        a_in = input('YES/NO: ')
                        
                        if a_in.lower() == 'yes':
                            print('GROUP ZERO PRESENT')
                            time.sleep(1)
                            print('The gas evolved on passing through Nessler Reagent gives brown precipitate.')
                            time.sleep(1)
                            print('Congratulations, you got Ammonia as your cation!')
                        else:
                            print('Then, Dilute Hydrochloric Acid was added. Did you see any type of white ppt.?')
                            b_in = input('YES/NO: ')
                            if b_in.lower() == 'yes':
                                print('GROUP ONE PRESENT. Group One contains Lead.')
                            else:
                                print('Then, we pass hydrogen sulphide gas through it. Did it form any kind of Black/yellow Ppt.?')
                                c_in = input('YES/NO: ')
                                if c_in.lower() == 'yes':
                                    print('GROUP TWO PRESENT. Group Two contains Lead, Copper and Arsenic.')
                                else:
                                    print('Then we take Original Solution, add conc. Nitric Acid, boil, add solid Ammonium Chloride and Ammonium Hydroxide. Did you notice brown or green/white gelatinous ppt.?')
                                    d_in = input('YES/NO: ')
                                    if d_in.lower() == 'yes':
                                        print('GROUP THREE PRESENT. Group Three contains Iron and Aluminium.')
                                    else:
                                        print('Then we pass Hydrogen Sulphide Gas through it. Do you notice white/flesh colored or black ppt.?')
                                        e_in = input('YES/NO: ')
                                        if e_in.lower() == 'yes':
                                            print('GROUP FOUR PRESENT. Group Four contains Nickel, Cobalt, Zinc and Manganese.')
                                        else:
                                            print('Then we take Original Solution, add solid Ammonium Chloride, Ammonium Hydroxide and Ammonium Carbonate. Do you notice white ppt.?')
                                            f_in = input('YES/NO: ')
                                            if f_in.lower() == 'yes':
                                                print('GROUP FIVE PRESENT. Group Five contains Barium, Strontium and Calcium.')
                                            else:
                                                print('Then we add Disodium Hydrogen Orthophosphate solution. Do you notice white ppt.?')
                                                g_in = input('YES/NO: ')
                                                if g_in.lower() == 'yes':
                                                    print('GROUP SIX PRESENT. Group Six contains Magnesium.')
                                                else:
                                                    print('Unknown Cation.')
                    elif choice_3==4:
                        break
            elif choice_2 == 3:
                break
            break

    # ---------------------------------------------------------
    # 2. ANION PRELIMINARY ANALYSIS
    # ---------------------------------------------------------
    elif choice_1 == 2:
        while True:
            print('\nDry sample was taken, dilute sulphuric acid was added to it.')
            print('Select your observation correctly:')
            print('1. Brisk effervescence without smell which turns lime water milky')
            print('2. Brisk effervescence with smell of rotten eggs and turns lead acetate paper shiny black')
            print('3. Colourless vapour with pungent smell of vinegar')
            print('4. None of these (Proceed to confirmatory acid tests)')
            
            a_anion = int(input('Enter choice number: '))
            if a_anion == 1:
                print('May be Carbonate Anion')
            elif a_anion == 2:
                print('May be Sulphide Anion')
            elif a_anion == 3:
                print('May be Acetate Anion')
            elif a_anion == 4:
                print('Add concentrated sulphuric acid to dry sample and heat. Bring a glass rod dipped in NH4OH near mouth.')
                b_anion = input('Do you notice dense white fumes? (YES/NO): ')
                if b_anion.lower() == 'yes':
                    print('May be Chloride anion')
                else:
                    print('Take sample, add copper turnings and conc. H2SO4 and heat.')
                    c_anion = input('Do you see brown fumes getting evolved? (YES/NO): ')
                    if c_anion.lower() == 'yes':
                        print('Nitrate may be present')
                    else:
                        print('Unknown anion.')
            break

    # ---------------------------------------------------------
    # 3. CATION CONFIRMATORY ANALYSIS
    # ---------------------------------------------------------
    elif choice_1 == 3:
        while True:
            print('\nWELCOME TO CONFIRMATORY ANALYSIS OF CATIONS.')
            print('1. GROUP ZERO\n2. GROUP ONE\n3. GROUP TWO\n4. GROUP THREE\n5. GROUP FOUR\n6. GROUP FIVE\n7. GROUP SIX\n8. EXIT TO MAIN MENU')
            
            time.sleep(1)
            j = int(input('Enter the choice number: '))
            
            if j == 1:
                print('Ammonium Cation present and confirmed')
            elif j == 2:
                print('Group One contains Lead. White ppt dissolved in hot water, treated with KI and K2CrO4 gave yellow ppts.')
                print('Lead present and confirmed')
            elif j == 3:
                print('Copper present and confirmed (Deep blue with excess NH4OH, chocolate brown with K4[Fe(CN)6])')
            elif j == 4:
                print('Group Three contains Iron and Aluminium.')
                k = input('Did Ammonium Thiocyanate give Blood red colouration? (YES/NO): ')
                if k.lower() == 'yes':
                    print('Iron present and confirmed')
                else:
                    m = input('Did Potassium Ferrocyanide give Prussian Blue ppt? (YES/NO): ')
                    if m.lower() == 'yes':
                        print('Iron Present and confirmed')
                    else:
                        p = input('Did white gelatinous ppt dissolve in excess Sodium Hydroxide? (YES/NO): ')
                        if p.lower() == 'yes':
                            print('Aluminium present and confirmed')
                        else:
                            print('Unknown cation')
            elif j == 5:
                t = input('Was white ppt soluble in excess Sodium Hydroxide or Ammonium Hydroxide? (YES/NO): ')
                if t.lower() == 'yes':
                    print('Zinc present and confirmed')
                else:
                    q = input('Was there a bright red ppt with Dimethyl Glyoxime? (YES/NO): ')
                    if q.lower() == 'yes':
                        print('Nickel present and confirmed')
                    else:
                        w = input('Did the ether layer turn blue with Ammonium Thiocyanate? (YES/NO): ')
                        if w.lower() == 'yes':
                            print('Cobalt present and confirmed')
                        else:
                            v = input('Was there any flesh colored ppt with Sodium Hydroxide? (YES/NO): ')
                            if v.lower() == 'yes':
                                print('Manganese present and confirmed')
                            else:
                                print('Unknown Cation')
            elif j == 6:
                a_grp5 = input('Did Potassium Chromate give yellow ppt? (YES/NO): ')
                if a_grp5.lower() == 'yes':
                    print('Barium present and confirmed')
                else:
                    b_grp5 = input('Did Ammonium Sulphate give white ppt? (YES/NO): ')
                    if b_grp5.lower() == 'yes':
                        print('Strontium Present and confirmed')
                    else:
                        c_grp5 = input('Did Ammonium Oxalate give white ppt? (YES/NO): ')
                        if c_grp5.lower() == 'yes':
                            print('Calcium present and confirmed')
                        else:
                            print('Unknown Cation')
            elif j == 7:
                e_grp6 = input('Did Disodium Hydrogen Orthophosphate give white ppt? (YES/NO): ')
                if e_grp6.lower() == 'yes':
                    print('Magnesium present and confirmed')
                else:
                    print('Unknown Cation')
            elif j == 8:
                break

    # ---------------------------------------------------------
    # 4. ANION CONFIRMATORY ANALYSIS
    # ---------------------------------------------------------
    elif choice_1 == 4:
        while True:
            print('\nWELCOME TO ANION CONFIRMATORY ANALYSIS')
            time.sleep(1)
            print('A small amount of sample solution was acidified with dil. Hydrochloric Acid and Barium Chloride was added.')
            a_anconf = input('Did you notice white ppt insoluble in mineral acids? (YES/NO): ')
            if a_anconf.lower() == 'yes':
                print('Sulphate present and confirmed')
            else:
                b_anconf = input('Did Silver Nitrate with Nitric Acid give white ppt soluble in Ammonium Hydroxide? (YES/NO): ')
                if b_anconf.lower() == 'yes':
                    print('Chloride present and confirmed')
                else:
                    g_anconf = input('Was there a Brown ring formed with iron Sulphate and conc. sulphuric acid? (YES/NO): ')
                    if g_anconf.lower() == 'yes':
                        print('Nitrate present and confirmed')
                    else:
                        j_anconf = input('Did sodium nitroprusside give violet colour? (YES/NO): ')
                        if j_anconf.lower() == 'yes':
                            print('Sulphide present and confirmed')
                        else:
                            k_anconf = input('Did neutral Iron (iii) Chloride give reddish color disappearing with dil. HCl? (YES/NO): ')
                            if k_anconf.lower() == 'yes':
                                print('Acetate present and confirmed')
                            else:
                                m_anconf = input('Did Calcium Chloride with acetic acid give white ppt soluble in dil. hydrochloric acid/nitric acid? (YES/NO): ')
                                if m_anconf.lower() == 'yes':
                                    print('Oxalate present and confirmed')
                                else:
                                    p_anconf = input('Did ammonium molybdate with conc. Nitric Acid give canary yellow ppt? (YES/NO): ')
                                    if p_anconf.lower() == 'yes':
                                        print('Phosphate present and confirmed')
                                    else:
                                        print('Unknown Anion')
            break

    # ---------------------------------------------------------
    # 5. EXIT
    # ---------------------------------------------------------
    elif choice_1 == 5:
        print('Exiting simulator')
        break
    else:
        print('Invalid option selected. Please choose between 1 and 5.')
