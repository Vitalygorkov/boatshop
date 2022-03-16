const rangeSlider = document.getElementById('range-slider-price');

if (rangeSlider) {
  noUiSlider.create(rangeSlider, {
    start: [500,999999],
    connect: true,
    step: 50,
    range: {
      'min': [500],
      'max': [999999]
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
