
var params = window.location.search.replace( '?', '').split('&').reduce(
        function(p,e){
            var a = e.split('=');
            p[ decodeURIComponent(a[0])] = decodeURIComponent(a[1]);
            return p;
        },
        {}
    );
console.log(params.price__lt);
// price
//const rangeSliderInit = () => { // создаем функцию инициализации слайдера
//  const range = document.getElementById('range-slider-price'); // Ищем слайдер
//  const inputMin = document.getElementById('input-price-0'); // Ищем input с меньшим значнием
//  const inputMax = document.getElementById('input-price-1'); // Ищем input с большим значнием
//
//  if (!range || !inputMin || !inputMax) return // если этих элементов нет, прекращаем выполнение функции, чтобы не было ошибок
//
//  const inputs = [inputMin, inputMax]; // создаем массив из меньшего и большего значения
//
//  noUiSlider.create(range, { // инициализируем слайдер
//      start: [0, 100000], // устанавливаем начальные значения
//      connect: true, // указываем что нужно показывать выбранный диапазон
//      range: { // устанавливаем минимальное и максимальное значения
//        'min': 0,
//        'max': 100000
//      },
//      step: 1, // шаг изменения значений
//    }
//  )
//
//  range.noUiSlider.on('update', function (values, handle) { // при изменений положения элементов управления слайдера изменяем соответствующие значения
//    inputs[handle].value = parseInt(values[handle]);
//  });
//
//  inputMin.addEventListener('change', function () { // при изменении меньшего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([this.value, null]);
//  });
//
//  inputMax.addEventListener('change', function () { // при изменении большего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([null, this.value]);
//  });
//
//}
//const init = () => {
//  rangeSliderInit() // запускаем функцию инициализации слайдера
//}
//window.addEventListener('DOMContentLoaded', init) // запускаем функцию init, когда документ будет загружен и готов к взаимодействию
//
////length
//const rangeSliderLengthInit = () => { // создаем функцию инициализации слайдера
//  const range = document.getElementById('range-slider-length'); // Ищем слайдер
//  const inputMin = document.getElementById('input-length-0'); // Ищем input с меньшим значнием
//  const inputMax = document.getElementById('input-length-1'); // Ищем input с большим значнием
//  if (!range || !inputMin || !inputMax) return // если этих элементов нет, прекращаем выполнение функции, чтобы не было ошибок
//  const inputs = [inputMin, inputMax]; // создаем массив из меньшего и большего значения
//  noUiSlider.create(range, { // инициализируем слайдер
//      start: [0, 600], // устанавливаем начальные значения
//      connect: true, // указываем что нужно показывать выбранный диапазон
//      range: { // устанавливаем минимальное и максимальное значения
//        'min': 0,
//        'max': 600
//      },
//      step: 1, // шаг изменения значений
//    }
//  )
//  range.noUiSlider.on('update', function (values, handle) { // при изменений положения элементов управления слайдера изменяем соответствующие значения
//    inputs[handle].value = parseInt(values[handle]);
//  });
//  inputMin.addEventListener('change', function () { // при изменении меньшего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([this.value, null]);
//  });
//  inputMax.addEventListener('change', function () { // при изменении большего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([null, this.value]);
//  });
//}
//const initLength = () => {
//  rangeSliderLengthInit() // запускаем функцию инициализации слайдера
//}
//window.addEventListener('DOMContentLoaded', initLength) // запускаем функцию init, когда документ будет загружен и готов к взаимодействию

////width
//const rangeSliderWidthInit = () => { // создаем функцию инициализации слайдера
//  const range = document.getElementById('range-slider-width'); // Ищем слайдер
//  const inputMin = document.getElementById('input-width-0'); // Ищем input с меньшим значнием
//  const inputMax = document.getElementById('input-width-1'); // Ищем input с большим значнием
//  if (!range || !inputMin || !inputMax) return // если этих элементов нет, прекращаем выполнение функции, чтобы не было ошибок
//  const inputs = [inputMin, inputMax]; // создаем массив из меньшего и большего значения
//  noUiSlider.create(range, { // инициализируем слайдер
//      start: [0, 100000], // устанавливаем начальные значения
//      connect: true, // указываем что нужно показывать выбранный диапазон
//      range: { // устанавливаем минимальное и максимальное значения
//        'min': 0,
//        'max': 100000
//      },
//      step: 1, // шаг изменения значений
//    }
//  )
//  range.noUiSlider.on('update', function (values, handle) { // при изменений положения элементов управления слайдера изменяем соответствующие значения
//    inputs[handle].value = parseInt(values[handle]);
//  });
//  inputMin.addEventListener('change', function () { // при изменении меньшего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([this.value, null]);
//  });
//  inputMax.addEventListener('change', function () { // при изменении большего значения в input - меняем положение соответствующего элемента управления
//    range.noUiSlider.set([null, this.value]);
//  });
//}
//const init = () => {
//  rangeSliderWidthInit() // запускаем функцию инициализации слайдера
//}
//window.addEventListener('DOMContentLoaded', init) // запускаем функцию init, когда документ будет загружен и готов к взаимодействию


 //цена
const rangeSlider = document.getElementById('range-slider-price');
if (rangeSlider) {
  noUiSlider.create(rangeSlider, {
    start: [0,299999],
    connect: true,
    step: 10,
    range: {
      'min': [0],
      'max': [299999]
    },
  });
  const input0 = document.getElementById('input-price-0');
  const input1 = document.getElementById('input-price-1');
  const inputs = [input0, input1];
      rangeSlider.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSlider.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}
