
var params = window.location.search.replace( '?', '').split('&').reduce(
        function(p,e){
            var a = e.split('=');
            p[ decodeURIComponent(a[0])] = decodeURIComponent(a[1]);
            return p;
        },
        {}
    );
console.log(params.price__lt);

// Цена
const rangeSlider = document.getElementById('range-slider-price');

if (rangeSlider) {
  noUiSlider.create(rangeSlider, {
    start: [params.price__gt,params.price__lt],
    connect: true,
    step: 10,
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

// длина
const rangeSlider2 = document.getElementById('range-slider-length');

if (rangeSlider2) {
  noUiSlider.create(rangeSlider2, {
    start: [params.length__gt,params.length__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [550]
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
    start: [params.width__gt,params.width__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [220]
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

// длина кокпита
const rangeSliderCockpitLength = document.getElementById('range-slider-cockpit-length');
if (rangeSliderCockpitLength) {
  noUiSlider.create(rangeSliderCockpitLength, {
    start: [params.cockpit_length__gt,params.cockpit_length__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [500]
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
    start: [params.cockpit_width__gt,params.cockpit_width__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [200]
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
    start: [params.load_capacity__gt,params.load_capacity__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [1200]
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
    start: [params.boat_weight__gt,params.boat_weight__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [150]
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
    start: [params.complete_set_weight__gt,params.complete_set_weight__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [180]
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
    start: [params.maximum_motor_power__gt,params.maximum_motor_power__lt],
    connect: true,
    step: 1,
    range: {
      'min': [0],
      'max': [100]
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
    start: [params.fabric_thickness_side__gt,params.fabric_thickness_side__lt],
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
    start: [params.fabric_thickness_bottom__gt,2000],
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
    start: [params.inflatable_compartments__gt,params.inflatable_compartments__lt],
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
    start: [params.passenger_capacity__gt,params.passenger_capacity__lt],
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
