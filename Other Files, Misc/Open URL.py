import webbrowser
import keyboard
a=input("what URL should I open?  ")
b=1
c=2
while b<c:
  url = a
  webbrowser.open_new_tab(url)
  try:
    if keyboard.is_pressed('h'):
      b=100
  except:pass
print("Thanks")
