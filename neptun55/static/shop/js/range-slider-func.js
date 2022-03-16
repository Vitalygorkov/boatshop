
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
    step: 50,
    range: {
      'min': [0],
      'max': [299999]
    }
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

// длинна
const rangeSlider2 = document.getElementById('range-slider-length');
if (rangeSlider2) {
  noUiSlider.create(rangeSlider2, {
    start: [0,600],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [600]
    }
  });
  const input0 = document.getElementById('input-length-0');
  const input1 = document.getElementById('input-length-1');
  const inputs = [input0, input1];
  rangeSlider2.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSlider2.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// ширина
const rangeSliderWidth = document.getElementById('range-slider-width');
if (rangeSliderWidth) {
  noUiSlider.create(rangeSliderWidth, {
    start: [0,250],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [250]
    }
  });
  const input0 = document.getElementById('input-width-0');
  const input1 = document.getElementById('input-width-1');
  const inputs = [input0, input1];
  rangeSliderWidth.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderWidth.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// длинна кокпита
const rangeSliderCockpitLength = document.getElementById('range-slider-cockpit-length');
if (rangeSliderCockpitLength) {
  noUiSlider.create(rangeSliderCockpitLength, {
    start: [0,600],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [600]
    }
  });
  const input0 = document.getElementById('input-cockpit-length-0');
  const input1 = document.getElementById('input-cockpit-length-1');
  const inputs = [input0, input1];
  rangeSliderCockpitLength.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderCockpitLength.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// ширина кокпита
const rangeSliderCockpitWidth = document.getElementById('range-slider-cockpit_width');
if (rangeSliderCockpitWidth) {
  noUiSlider.create(rangeSliderCockpitWidth, {
    start: [0,250],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [250]
    }
  });
  const input0 = document.getElementById('input-cockpit-width-0');
  const input1 = document.getElementById('input-cockpit-width-1');
  const inputs = [input0, input1];
  rangeSliderCockpitWidth.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderCockpitWidth.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Грузоподъемность
const rangeSliderLoadCapacity = document.getElementById('range-slider-load-capacity');
if (rangeSliderLoadCapacity) {
  noUiSlider.create(rangeSliderLoadCapacity, {
    start: [0,2500],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [2500]
    }
  });
  const input0 = document.getElementById('input-load-capacity-0');
  const input1 = document.getElementById('input-load-capacity-1');
  const inputs = [input0, input1];
  rangeSliderLoadCapacity.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderLoadCapacity.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Вес лодки
const rangeSliderBoatWeight = document.getElementById('range-slider-boat-weight');
if (rangeSliderBoatWeight) {
  noUiSlider.create(rangeSliderBoatWeight, {
    start: [0,2500],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [2500]
    }
  });
  const input0 = document.getElementById('input-boat-weight-0');
  const input1 = document.getElementById('input-boat-weight-1');
  const inputs = [input0, input1];
  rangeSliderBoatWeight.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderBoatWeight.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Вес полного комплекта
const rangeSliderCompleteSetWeight = document.getElementById('range-slider-complete-set-weight');
if (rangeSliderCompleteSetWeight) {
  noUiSlider.create(rangeSliderCompleteSetWeight, {
    start: [0,2500],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [2500]
    }
  });
  const input0 = document.getElementById('input-complete-set-weight-0');
  const input1 = document.getElementById('input-complete-set-weight-1');
  const inputs = [input0, input1];
  rangeSliderCompleteSetWeight.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderCompleteSetWeight.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Макс мощность мотора
const rangeSliderMaximumMotorPower = document.getElementById('range-slider-maximum-motor-power');
if (rangeSliderMaximumMotorPower) {
  noUiSlider.create(rangeSliderMaximumMotorPower, {
    start: [0,150],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [150]
    }
  });
  const input0 = document.getElementById('input-maximum-motor-power-0');
  const input1 = document.getElementById('input-maximum-motor-power-1');
  const inputs = [input0, input1];
  rangeSliderMaximumMotorPower.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderMaximumMotorPower.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Плотность ткани борта
const rangeSliderFabricThicknessSide = document.getElementById('range-slider-fabric-thickness-side');
if (rangeSliderFabricThicknessSide) {
  noUiSlider.create(rangeSliderFabricThicknessSide, {
    start: [0,2000],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [2000]
    }
  });
  const input0 = document.getElementById('input-fabric-thickness-side-0');
  const input1 = document.getElementById('input-fabric-thickness-side-1');
  const inputs = [input0, input1];
  rangeSliderFabricThicknessSide.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderFabricThicknessSide.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Плотность ткани дна
const rangeSliderFabricThicknessBottom = document.getElementById('range-slider-fabric-thickness-bottom');
if (rangeSliderFabricThicknessBottom) {
  noUiSlider.create(rangeSliderFabricThicknessBottom, {
    start: [0,2000],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [2000]
    }
  });
  const input0 = document.getElementById('input-fabric-thickness-bottom-0');
  const input1 = document.getElementById('input-fabric-thickness-bottom-1');
  const inputs = [input0, input1];
  rangeSliderFabricThicknessBottom.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderFabricThicknessBottom.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}

// Количество надувных отсеков
const rangeSliderInflatableCompartments = document.getElementById('range-slider-inflatable-compartments');
if (rangeSliderInflatableCompartments) {
  noUiSlider.create(rangeSliderInflatableCompartments, {
    start: [0,15],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [15]
    }
  });
  const input0 = document.getElementById('input-inflatable-compartments-0');
  const input1 = document.getElementById('input-inflatable-compartments-1');
  const inputs = [input0, input1];
  rangeSliderInflatableCompartments.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderInflatableCompartments.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}


// Пассажировместимость
const rangeSliderPassengerCapacity = document.getElementById('range-slider-passenger-capacity');
if (rangeSliderPassengerCapacity) {
  noUiSlider.create(rangeSliderPassengerCapacity, {
    start: [0,15],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [15]
    }
  });
  const input0 = document.getElementById('input-passenger-capacity-0');
  const input1 = document.getElementById('input-passenger-capacity-1');
  const inputs = [input0, input1];
  rangeSliderPassengerCapacity.noUiSlider.on('update', function(values, handle){
    inputs[handle].value = Math.round(values[handle]);
  });

  const setRangeSlider = (i, value) => {
    let arr = [null, null];
    arr[i] = value;

    rangeSliderPassengerCapacity.noUiSlider.set(arr);
  };
  inputs.forEach((el, index) =>{
    el.addEventListener('change', (e) => {
      setRangeSlider(index, e.currentTarget.value);
    });
  });
}
