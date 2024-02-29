var step_a = document.getElementById("text_box_1").innerHTML; // получил данные
var step_b = step_a.replace(/&lt;FC&gt;/g, '<a href="{% url 'as_search_results' %}?search='); // нашел тэг и поменял
var step_c = step_b.replace(/&lt;\/FC&gt;/g, '">FC<\/a>'); // записал новые данные

document.getElementById('text_box_1').innerHTML = step_c;

console.log(step_a);
console.log(step_b);
console.log(step_c);
