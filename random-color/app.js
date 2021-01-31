function displayCurrentColor() {
  const body = document.body.style.backgroundImage
  const title = document.getElementsByTagName('h2')[0]
  title.textContent = `body { height: 100vh; background-image: ${body} }`
}

displayCurrentColor()

function changeCurrentColor() {
  document.body.style.backgroundImage = `linear-gradient(to bottom right, #${randomHexCodeGenerator()}, #${randomHexCodeGenerator()})`;
  displayCurrentColor()
}

function randomHexCodeGenerator() {
  var randomColor = Math.floor(Math.random()*16777215).toString(16);
  return randomColor
}