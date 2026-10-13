"""
RECORD CHECK  -  my version
===========================

Name  : Nicole 
Lane  :  AI 
Date  :25/09/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

hostname = input("Hostname: ")
gb_used = float(input("First value: "))    
gb_total = float(input("Second value: "))    


gb_free = gb_total - gb_used
percent_used = (gb_used / gb_total) * 100


percent_free = 100 - percent_used

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used        : {gb_used:>10.2f}")
print(f"  Total       : {gb_total:>10.2f}")
print(f"  Free        : {gb_free:>+10.2f}")
print(f"  Percent     : {percent_used:>10.2f} %")
print(f"  Percent free: {percent_free:>10.2f} %")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
