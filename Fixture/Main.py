import random
Teams = []
TeamsList = []
Fixture = []
Fixture2 = []
Part1 = []
Part2 = []
a = 0
rounds = 1
Teams.append("Fenerbahce")
Teams.append("Galatasaray")
Teams.append("Besiktas")
Teams.append("Trabzonspor")
Teams.append("Sivasspor")
if (len(Teams) % 2):
  Teams.append("Bay")
while(rounds < len(Teams)):
  TeamsList = Teams.copy()
  Fixture.append(f"Round {rounds}")
  Fixture2.append(f"Round {rounds + len(Teams) - 1}")
  while(len(TeamsList)):
    a += 1     # Bazen maç seçimi yapılıp takımlar listeden silinince listede kalan takımlar birbirleri ile maç yapmış olabiliyor bu yüzden kalan takımları fiksüre ekleyemediğinden
    # sonsuz döngüye giriyor. burada a değişkenini sayaç olarak tutuyorum eğer listeye ekleme yapılamıyorsa artacak aşağıda da her listeye ekleme yapıldığında sıfırlanacak
    # Eğer 50 kadar seçim yapıp hiçbirini listeye ekleyemiyorsa kalan takımlar birbiri ile eşleşemiyor demek bu yüzden de o haftanın fiksürü olarak listeyi temizleyip o haftaki 
    # fiksürü yeniden çekeceğiz.
    Matches = ""
    FirstT = random.choice(TeamsList)
    SecondT = random.choice(TeamsList)
    if FirstT != SecondT:
      Matches = FirstT + " vs " + SecondT
      if ((Matches not in Part1) and (Matches not in Part2)):
        a = 0
        Fixture.append(Matches)
        Fixture2.append(SecondT + " vs " + FirstT)
        TeamsList.remove(FirstT)
        TeamsList.remove(SecondT)
    if (a > 50):
      Fixture.clear()
      Fixture2.clear
      Fixture.append(f"Round {rounds}")
      Fixture2.append(f"Round {rounds + len(Teams) - 1}")
      TeamsList = Teams.copy()
      a = 0
  for i in Fixture:  # for un kısa kullanımı ile yapamıyorum çünkü listenin içindeki bilgileri silip son fiksürü yazıyor.
    Part1.append(i)
  for j in Fixture2:
    Part2.append(j)
  TeamsList.clear()
  rounds += 1
  Fixture.clear()
  Fixture2.clear()

for i in Part1:
  print(i)
for j in Part2:
  print(j)