import os
chapters = []
for i in range(17):
  chapters.append( "chapter_%02d" % (i+1))
chapters.append("chapter_A1")
chapters.append("chapter_A2")

contributors = ["Katya", "Kelsey", "Jacob", "Peter", "Ryan"]

for chapter in chapters:
  if not os.path.exists("./"+chapter):
    os.makedirs("./"+chapter)
  for contrib in contributors:
    notes = "notes_%s.py" % (contrib)
    locus =  "./"+chapter+"/"+notes
    # if not os.path.exists(locus)
    open(locus, 'a').close()
