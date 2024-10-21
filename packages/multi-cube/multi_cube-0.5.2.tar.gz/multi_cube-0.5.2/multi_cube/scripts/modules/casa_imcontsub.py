import sys


args = sys.argv
for item in sys.argv:
    parts = item.split('=')
    if parts[0] == 'mycube':
        mycubefits = parts[1]
    elif parts[0] == 'imfitorder':
        imfitorder = int(parts[1])
print(f" These are the arguments for cas imcontsub.py {args}")

mycubecasa = mycubefits.replace('.fits','.im')

importfits(fitsimage=mycubefits,imagename=mycubecasa,overwrite=True)

imcontsub(imagename=mycubecasa,fitorder=imfitorder,linefile=mycubecasa+'.linefile',contfile=mycubecasa+'.contfile') 

exportfits_name = mycubecasa.replace('.im','.linefile.fits')

exportfits(imagename=mycubecasa+'.linefile',fitsimage=exportfits_name,overwrite=True)
os.system('rm -fr %s'%mycubecasa)