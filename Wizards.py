class Wizards:
    def __init__(self):
        # open file
        xfile = open("spells.txt")

        # construct a dictionary with spell name and it's power (every wizard with his own spells)
        self.spells_pow_dic = {}
        for line in xfile:
            line = line.rstrip()
            words = line.split()
            # if first letter is A this means the corrsponding spell is common and can be used by the two wizards
            # so i add this common spell two times, one for harry and one for voldmort (i.e HCrucio, VCrucio)
            # I did this so I can know wether the user has entered the right spell for right wizard or not
            if words[0] =='A':
                name = 'H' + words[1]
                self.spells_pow_dic[name] = words[2]
                name = 'V' + words[1]
                self.spells_pow_dic[name] = words[2]
            # if first litter isn't A then the spell is added once for the corrsponding wizard
            else:
                name = words[0] + words[1]
                self.spells_pow_dic[name] = words[2]
        # close the file
        xfile.close()
        print(self.spells_pow_dic)

        # intilaize the the wizirads health and energy
        self.h_health = 100
        self.h_energy = 500
        self.v_health = 100
        self.v_energy = 500

    # battle function to handle the battle
    def battle(self):
        while self.h_health > 0 and self.v_health > 0:
            # take spells names from user
            spells = input("Enter the two spills (H then V): ")
            spells_lst = spells.split()


            # get spells power from constructed dictionary above and check if user enterd right spell for right wizard
            if 'H' + spells_lst[0] in list(self.spells_pow_dic.keys()) and 'V' + spells_lst[1] in list(self.spells_pow_dic.keys()):
                h_spell_pow = self.spells_pow_dic.get('H' + spells_lst[0])
                v_spell_pow = self.spells_pow_dic.get('V' + spells_lst[1])
            else:
                print("You entered a spell that doesn't belong to the wizard!")
                continue

            # calculate new energy
            self.h_energy = self.h_energy - int(h_spell_pow)
            self.v_energy = self.v_energy - int(v_spell_pow)

            # calculate new health
            if int(h_spell_pow) != 0 and int(v_spell_pow) != 0:
                if int(h_spell_pow) > int(v_spell_pow):
                    self.v_health = self.v_health - (int(h_spell_pow) - int(v_spell_pow))
                else:
                    self.h_health = self.h_health - (int(v_spell_pow) - int(h_spell_pow))


            if self.h_health < 0:
                self.h_health = 0
            if self.v_health < 0:
                self.v_health = 0

            # print the result of this round using print_results function
            self.print_results()

        # check end of the battle and printing the winner name
        if self.h_health <= 0:
            print("Voldmort is the winner")
        elif self.v_health <= 0:
            print("Harry Potter is the winner")

    def print_results(self):
        print("       Harry            Voldmort")
        print("Health: %d              %d" % (self.h_health, self.v_health))
        print("Energy: %d              %d" % (self.h_energy, self.v_energy))

