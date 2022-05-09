
var stamp_d = '';

function main_print(sub_menu = 'presets', cur_id = 'bartender_m1', swatch_id = 'default'){
	
	
	const print_to = document.getElementById('viewport');
	
	const graphic_info = graphics[cur_id];
	
	let choose_presets =``;
	Object.keys(graphics).forEach(function(preset){
		
		choose_presets += `<button class="preset" id="${preset}" data-id="${preset}" onclick="main_print('presets', '${preset}', '${swatch_id}')">><svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">${get_svg_code(graphics[preset], 'white')}</svg></button>`;
		
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
	</div>
	<div id="export_buttons">
		<button id="export" onclick="save_character_image();">Export as SVG</button>
		<button id="export" onclick="save_character_image('webp');">Export as WEBP</button>
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
		else if(info == 'path'){
			fill_color = (print_in_white == 'white') ? '#fff' : 'url(#acc_grad)';
			portrait_print += `<path class="${info}" fill="${fill_color}" d="${obj[info]}" />`;
			stamp_d += obj[info];
		}
		else if( Object.prototype.toString.call( obj[info] ) === '[object Object]' ){
			portrait_print += `<g class="${info}">${get_svg_code(obj[info], print_in_white)}</g>`;
		}
		else {
			const fill_value = ( swatches[print_in_white].values.face.hasOwnProperty(info) ) ? swatches[print_in_white].values.face[info] : swatches[print_in_white].values[info];
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