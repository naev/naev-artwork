
var stamp_d = '';

function main_print(sub_menu = 'presets', cur_id = 'bartender_m1', swatch_id = 'default'){
	
	stamp_d ='';
	
	const print_to = document.getElementById('viewport');
	
	const graphic_info = graphics[cur_id];
	
	let choose_presets =``;
	Object.keys(graphics).forEach(function(preset){
		
		choose_presets += `<button class="preset" id="${preset}" data-id="${preset}" onclick="main_print('presets', '${preset}', '${swatch_id}')">><svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">${get_svg_code(graphics[preset], true)}</svg></button>`;
		
	});
	
	let choose_swatches =``;
	Object.keys(swatches).forEach(function(swatch){
		
		choose_swatches += `<button class="swatch" id="${swatch}" data-id="${swatch}" onclick="main_print('swatches', '${cur_id}', '${swatch}')">${swatches[swatch].label}</button>`;
		
	});
	
	const menu_html = `<div id="main_menu" class="${sub_menu}">
		<div id="choose_submenu">
			<button onclick="change_parent_class('presets', this)">Presets</button>
			<button onclick="change_parent_class('swatches', this)">Colors</button>
		</div>
		<div id="presets"><h2>Choose Preset</h2>${choose_presets}</div>
		<div id="swatches"><h2>Choose Colors</h2>${choose_swatches}</div>
	</div>`;
	
	
	
	let portrait_print = '';
	
		
	portrait_print += get_svg_code(graphic_info);
	
	const portrait_html = `<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">
		<path class="stamp" fill="#fff" stroke-width="20" stroke="#fff" stroke-linejoin="round" d="${stamp_d}" />
		${portrait_print}
	</svg>`;
		
	
	
	
	print_to.innerHTML = menu_html + portrait_html;
}
window.onload = function(){
	
	main_print();

}

function get_svg_code(obj, print_in_white = false){
	let portrait_print ='';
	let fill_color = '';
	
	Object.keys(obj).forEach(function(info){
		if(info == 'defs'){
			portrait_print += obj[info];
		}
		else if(info == 'path'){
			fill_color = (print_in_white) ? '#fff' : 'url(#acc_grad)';
			portrait_print += `<path class="${info}" fill="${fill_color}" d="${obj[info]}" />`;
			stamp_d += obj[info];
		}
		else if( Object.prototype.toString.call( obj[info] ) === '[object Object]' ){
			portrait_print += `<g class="${info}">${get_svg_code(obj[info], print_in_white)}</g>`;
		}
		else {
			const fill_value = ( swatches.default.values.face.hasOwnProperty(info) ) ? swatches.default.values.face[info] : swatches.default.values[info];
			fill_color = (info == 'lines') ? '000' : ((print_in_white) ? 'fff' : fill_value);
			
			portrait_print += `<path class="${info}" fill="#${fill_color}" d="${obj[info]}" />`;
			stamp_d += obj[info];
		}
	});
	
	return portrait_print;
}

function change_parent_class(change_to = '', obj){
	obj.parentNode.parentNode.classList = change_to;
	
}