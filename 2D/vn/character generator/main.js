
var stamp_d = '';

function main_print(sub_menu = 'presets', cur_id = temp_char.preset, swatch_id = (swatches.hasOwnProperty('custom')) ? 'custom' : 'default'){
	
	temp_char.preset = cur_id;
	
	const print_to = document.getElementById('viewport');
	
	const graphic_info = graphics[cur_id];
	
	let choose_presets =``;
	Object.keys(graphics).forEach(function(preset){
		
		choose_presets += `<button class="preset" id="${preset}" data-id="${preset}" onclick="main_print('presets', '${preset}', '${swatch_id}')"><svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">${get_svg_code(graphics[preset], 'white')}</svg></button>`;
		
	});
	
	let choose_swatches =``;
	Object.keys(swatches).forEach(function(swatch){
		
		choose_swatches += `<button class="swatch" id="${swatch}" data-id="${swatch}" onclick="main_print('swatches', '${cur_id}', '${swatch}')">
			<span>${swatches[swatch].label}</span>
			<div class="swatch_gradient" style="background:linear-gradient(90deg, #${swatches[swatch].values.skin} 0%, #${swatches[swatch].values.skin} 25%, #${swatches[swatch].values.main} 25%, #${swatches[swatch].values.main} 50%, #${swatches[swatch].values.sec} 50%, #${swatches[swatch].values.sec} 75%, #${swatches[swatch].values.trim} 75%, #${swatches[swatch].values.trim} 100%);"></div>
		</button>`;
		
	});
	
	let choose_colors =``;
	Object.keys(swatches[swatch_id].values).forEach(function(color_option){
		
		if(color_option == 'face'){
			Object.keys(swatches[swatch_id].values.face).forEach(function(face_color_option){
				choose_colors += `<input id="picker_${face_color_option}" onchange="update_color('${face_color_option}', 'colors', '${cur_id}', '${swatch_id}', this)" value="#${swatches[swatch_id].values.face[face_color_option]}" type="color" title="${face_color_option}" />`;
			});
		}
		else if(color_option != 'acc_path'){
			choose_colors += `<input id="picker_${color_option}" onchange="update_color('${color_option}', 'colors', '${cur_id}', '${swatch_id}', this)" value="#${swatches[swatch_id].values[color_option]}" type="color" title="${color_option}" />`;
		}
	});
	
	const menu_html = `<div id="main_menu" class="${sub_menu}">
		<div id="choose_submenu">
			<button onclick="change_parent_class('presets', this)">Presets</button>
			<button onclick="change_parent_class('swatches', this)">Swatches</button>
			<button onclick="change_parent_class('colors', this)">Colors</button>
		</div>
		<div id="presets"><h2>Choose Preset</h2>${choose_presets}</div>
		<div id="swatches"><h2>Choose Color Swatch</h2>${choose_swatches}</div>
		<div id="colors">
			<h2>Choose Colors</h2>
			<div id="input_holder">${choose_colors}</div>
		</div>
	</div>
	<div id="export_buttons">
		<button id="export" onclick="save_character_image();">Export as SVG</button>
		<!--<button id="export" onclick="save_character_image('webp');">Export as WEBP</button>-->
	</div>`;
	
	
	
	let portrait_print = '';
	
	stamp_d ='';
		
	portrait_print += get_svg_code(graphic_info, swatch_id);
	
	const portrait_html = `<canvas id="hidden_canvas" width="1000" height="1415"></canvas>
	<div id="linkholder"></div>
	<svg id="main_portrait" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">
		<path class="stamp" fill="#fff" stroke-width="20" stroke="#fff" stroke-linejoin="round" d="${stamp_d}" />
		${portrait_print}
	</svg>`;
		
	
	
	
	print_to.innerHTML = menu_html + portrait_html;
}
window.onload = function(){
	
	main_print();

}

function get_svg_code(obj, print_in_white = 'default'){
	let portrait_print ='';
	let fill_color = '';
	
	Object.keys(obj).forEach(function(info){
		if(info == 'defs'){
			portrait_print += obj[info];
		}
		else if(info == 'goggles'){
			portrait_print += `<g class="${info}">${get_svg_code(obj[info][temp_char.goggles], print_in_white)}</g>`;
		}	
		else if(info == 'path'){
			fill_color = (print_in_white == 'white') ? '#fff' : 'url(#acc_grad)';
			portrait_print += `<path class="${info}" fill="${fill_color}" d="${obj[info]}" />`;
			stamp_d += obj[info];
		}
		else if( Object.prototype.toString.call( obj[info] ) === '[object Object]' ){
			portrait_print += `<g class="${info}">${get_svg_code(obj[info], print_in_white)}</g>`;
		}
		else {
			const fill_value = ( swatches[print_in_white].values.face.hasOwnProperty(info) ) ? swatches[print_in_white].values.face[info] : ((swatches[print_in_white].values.hasOwnProperty(info)) ? swatches[print_in_white].values[info] : swatches['default'].values[info]);
			fill_color = (info == 'lines') ? '000' : ((print_in_white == 'white') ? 'fff' : fill_value);
			
			portrait_print += `<path class="${info}" fill="#${fill_color}" d="${obj[info]}" />`;
			stamp_d += obj[info];
		}
	});
	
	return portrait_print;
}

function change_parent_class(change_to = '', obj){
	obj.parentNode.parentNode.classList = change_to;
	
}


function save_character_image(filetype = 'svg'){
	
	const svgElement = document.getElementById('main_portrait');
	
	const d = new Date();
	const t = d.getTime();
	
	if(filetype == 'svg') {
	
		const svg_pre = `<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
`;
		let serializer = new XMLSerializer();
		
		const source = svg_pre + serializer.serializeToString(svgElement);
		
		SAVE_KEY = `character_${t}`;
		
		hiddenElement = document.createElement('a');
		
		hiddenElement.href = 'data:attachment/svg+xml;charset=utf-8,' + encodeURIComponent(source);
		hiddenElement.target = '_blank';
		hiddenElement.download = SAVE_KEY + '.svg';
		hiddenElement.click();
		hiddenElement = null;
	
	}
	else if (filetype == 'webp'){
		
		let clonedSvgElement = svgElement.cloneNode(true);
		let outerHTML = clonedSvgElement.outerHTML,
		blob = new Blob([outerHTML],{type:'image/svg+xml;charset=utf-8'});

		let URL = window.URL || window.webkitURL || window;
		let blobURL = URL.createObjectURL(blob);
		  
		canvas = document.getElementById('hidden_canvas');
		
		let imageObj = new Image();
		imageObj.onload = () => {
			
		   canvas.width = 1000;
		   
		   canvas.height = 1415;
		   
		   let context = canvas.getContext('2d');
		   // draw image in canvas starting left-0 , top - 0  
		   context.drawImage(imageObj, 0, 0, 1000, 1415 );
		
		};
		imageObj.src = blobURL;
		
		//let png = canvas.toDataURL(); // default png
		//let jpeg = canvas.toDataURL('image/jpg', 0.85);
		let webp = canvas.toDataURL('image/webp', 1);
		
		let download = function(href, name){
		  let link = document.createElement('a');
		  link.download = name;
		  link.style.opacity = "0";
		  document.getElementById('linkholder').append(link);
		  link.href = href;
		  link.click();
		  link.remove();
		}
		
		setTimeout(function(){
			//download(png, `character_${t}.png`);
			download(webp, `character_${t}.webp`);
		}, 500);
		
		
	}
}

function update_color(part = false, c_sub_menu, c_cur_id, c_preset = 'default', obj){
	console.log(obj);
	const color_val = obj.value.split('#')[1];
	
	swatches['custom'] = {
		'label' : 'Custom',
		'values' : {
			'skin' 		: document.getElementById('picker_skin').value.split('#')[1],
			'main' 		: document.getElementById('picker_main').value.split('#')[1],
			'sec' 		: document.getElementById('picker_sec').value.split('#')[1],
			'trim' 		: document.getElementById('picker_trim').value.split('#')[1],
			'metal' 	: document.getElementById('picker_metal').value.split('#')[1],
			'dark_metal': document.getElementById('picker_dark_metal').value.split('#')[1],
			'orange'	: document.getElementById('picker_orange').value.split('#')[1],
			'green' 	: document.getElementById('picker_green').value.split('#')[1],
			'white' 	: document.getElementById('picker_white').value.split('#')[1],
			'nails' 	: document.getElementById('picker_nails').value.split('#')[1],
			'acc_path' 	: 'acc_grad',
			'towel' 	: document.getElementById('picker_towel').value.split('#')[1],
			'hair'		: document.getElementById('picker_hair').value.split('#')[1],
			'brows'		: document.getElementById('picker_brows').value.split('#')[1],
			'face' 		: {
				'eye_white' 	: document.getElementById('picker_eye_white').value.split('#')[1],
				'eye_color' 	: document.getElementById('picker_eye_color').value.split('#')[1],
				'lips' 		: document.getElementById('picker_lips').value.split('#')[1],
				'teeth' 	: document.getElementById('picker_teeth').value.split('#')[1],
			},
		},
	};
		
	/*
	if(swatches.custom.values.hasOwnProperty(part)){
		swatches.custom.values[part] = color_val;
	}
	if(swatches.custom.values.face.hasOwnProperty(part)){
		swatches.custom.values.face[part] = color_val;
	}
	*/
	main_print(c_sub_menu, c_cur_id, 'custom');
}