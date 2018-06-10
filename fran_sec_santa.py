#!/usr/bin/env python3.6
import random
import sys
from copy import copy


def secretSanta(scrublist, max_iters = 10):
   scrublist0 = scrublist.copy()
   scrubs = {k:'' for k in scrublist}
   niters = 0
   for scrub in scrubs.keys():
       if scrublist:
           randint = random.randrange(0, len(scrublist))
           while scrub == scrublist[randint]:
               randint = random.randrange(0, len(scrublist))
               niters += 1
               if niters > max_iters:
                   raise Exception("rip")

           scrubs[scrub] = scrublist[randint]
           scrublist.pop(randint)

   return scrubs


def secretSanta(scrublist):
    scrubs = {}
    scrublist = scrublist.copy()
    random.shuffle(scrublist)
    for k, v in zip(scrublist, scrublist[1:]):
        scrubs[k] = v

    scrubs[scrublist[-1]] = scrublist[0]
    return scrubs



def secretSanta(scrublist, max_iters = 10):
   scrublist0 = scrublist.copy()
   scrubs = {k:'' for k in scrublist}
   niters = 0
   for scrub in scrubs.keys():
       if scrublist:
           randint = random.randrange(0, len(scrublist))
           while scrub == scrublist[randint]:
               randint = random.randrange(0, len(scrublist))
               niters += 1
               if niters > max_iters:
                  return secretSanta(scrublist0)

           scrubs[scrub] = scrublist[randint]
           scrublist.pop(randint)

   return scrubs


if __name__ == '__main__':
   santaslist = sys.argv[1].split(" ")
   random.shuffle(santaslist)
   secretsl = secretSanta(santaslist)
   for elf, santa in secretsl.items():
       print("%s is %s's secret santa!" % (elf, santa))

