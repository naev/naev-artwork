
var stamp_d = '';

window.onload = function(){
	
	
	/*
	 * Assign Radnom Body Part Sizes
	 */
	
	temp_char.body.body = Math.floor(Math.random()*Object.keys(graphics).length);
	temp_char.colors = Object.keys(swatches)[Math.floor(Math.random()*Object.keys(swatches).length)];
	const char_preset = Object.keys(graphics)[temp_char.body.body];
	const graphic_info = graphics[char_preset];
	
	const hair_holder = Object.keys(graphic_info).filter(function(key_name){
		return key_name.indexOf("hair_") === 0;
	});
	
	let accessory_max = 0;
	if(graphic_info.hasOwnProperty('accessory') && graphic_info.accessory.hasOwnProperty('ver_1')) {
		accessory_max = Math.floor(Math.random()*Object.keys(graphic_info.accessory).length);
	} 
	
	let overtop_max = 0;
	if(graphic_info.hasOwnProperty('overtop') && graphic_info.overtop.hasOwnProperty('ver_1')) {
		overtop_max = Math.floor(Math.random()*Object.keys(graphic_info.overtop).length);
	}
	
	const random_variations = [
		((graphic_info.clothes.hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(graphic_info.clothes).length) : 0),
		((graphic_info.body.hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(graphic_info.body).length) : 0),
		((graphic_info.hasOwnProperty('head') && graphic_info.head.hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(graphic_info.head).length) : 0),
		(((hair_holder.length>0) && graphic_info[hair_holder[0]].hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(graphic_info[hair_holder[0]]).length) : 0),
		accessory_max,
		((graphic_info.hasOwnProperty('pet') && graphic_info.pet.hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(graphic_info.pet).length) : 0),
		overtop_max,
	];
	temp_char.clothes.clothes_v = random_variations[0];
	temp_char.body.body_v = random_variations[1];
	temp_char.body.head_v = random_variations[2];
	temp_char.body.hair_v = random_variations[3];
	temp_char.acc = random_variations[4];
	temp_char.pet = random_variations[5];
	temp_char.overtop = random_variations[6];
	
	
	//random face parts
	if(graphic_info.hasOwnProperty('head')){
		Object.keys(graphic_info.head).forEach(function(section_id){
			const section = graphic_info.head[section_id];
			temp_char.face[section_id] = (section.hasOwnProperty('ver_1')) ? Math.floor(Math.random()*Object.keys(section).length) : 0;
		});
	}
	
	/*
	 * Start
	 */
	setTimeout(function(){
		main_print('presets', char_preset, temp_char.colors, random_variations);
	},60);
	
	document.getElementById('version_holder').innerHTML = `Version ${version} | `;

}
function print_by_cat(category = 'neutral', args){
	
	const clothes_id = (args.hasOwnProperty('clothes_id')) ? args.clothes_id : false;
	const swatch_id = (args.hasOwnProperty('swatch_id')) ? args.swatch_id : false;
	const variation = (args.hasOwnProperty('variation')) ? args.variation : [0,0,0,0,0,0,0];
	temp_char.clothes.clothes_v = variation[0];
	temp_char.body.body_v = variation[1];
	temp_char.body.head_v = variation[2];
	temp_char.body.hair_v = variation[3];
	temp_char.acc = variation[4];
	temp_char.pet = variation[5];
	temp_char.overtop = variation[6];
	
	let face_variation = false;
	if(args.hasOwnProperty('face')){
		Object.keys(args.face).forEach(function(section_id){
			const section = args.face[section_id];
			temp_char.face[section_id] = section;
		});
	}
	
	let choose_presets =``;
	Object.keys(graphics).forEach(function(preset){
		if(graphics[preset].category == category){
			
			let variation_count = 0;
			let variation_options = '[';
			
			if(Object.keys(graphics[preset].clothes)[0].startsWith('ver_') && temp_char.clothes.clothes_v < Object.keys(graphics[preset].clothes).length){
				variation_options += temp_char.clothes.clothes_v + ','; 
				if(Object.keys(graphics[preset].clothes).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0,';
			}
			
			if(Object.keys(graphics[preset].body)[0].startsWith('ver_') && temp_char.body.body_v < Object.keys(graphics[preset].body).length){
				variation_options += temp_char.body.body_v + ',';
				if(Object.keys(graphics[preset].body).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0,';
			}
			
			if(graphics[preset].hasOwnProperty('head') && Object.keys(graphics[preset].head)[0].startsWith('ver_') && temp_char.body.head_v < Object.keys(graphics[preset].head).length){
				variation_options += temp_char.body.head_v + ',';
				if(Object.keys(graphics[preset].head).length>1){
					variation_count++;
				}
			} else { 
				variation_options += '0,';
			}
			
			if(graphics[preset].hasOwnProperty('hair_front') && Object.keys(graphics[preset].hair_front)[0].startsWith('ver_') && temp_char.body.hair_v < Object.keys(graphics[preset].hair_front).length) {
				variation_options += temp_char.body.hair_v + ',';
				
				if(Object.keys(graphics[preset].hair_front).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0,';
			}
			
			if(graphics[preset].hasOwnProperty('accessory') && Object.keys(graphics[preset].accessory)[0].startsWith('ver_') && temp_char.acc < Object.keys(graphics[preset].accessory).length) {
				variation_options += temp_char.acc + ',';
				
				if(Object.keys(graphics[preset].accessory).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0,';
			}
			
			if(graphics[preset].hasOwnProperty('pet') && Object.keys(graphics[preset].pet)[0].startsWith('ver_') && temp_char.pet < Object.keys(graphics[preset].pet).length) {
				variation_options += temp_char.pet + ',';
				
				if(Object.keys(graphics[preset].pet).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0,';
			}
			
			if(graphics[preset].hasOwnProperty('overtop') && Object.keys(graphics[preset].overtop)[0].startsWith('ver_') && temp_char.overtop < Object.keys(graphics[preset].overtop).length) {
				variation_options += temp_char.overtop + ']';
				
				if(Object.keys(graphics[preset].overtop).length>1){
					variation_count++;
				}
			}
			else {
				variation_options += '0]';
			}
			
			Object.keys(graphics[preset].head).forEach(function(section_id){
				const section = graphics[preset].head[section_id];
				
				if(Object.keys(section)[0].startsWith('ver_') && temp_char.face[section_id] < Object.keys(section).length){
					if(Object.keys(section).length>1){
						variation_count++;
					}
					
				}
				
				if( (clothes_id == preset) && (temp_char.face[section_id] >= Object.keys(section).length) ){
					temp_char.face[section_id] = Object.keys(section).length-1
				}
				
			});
			
			const plus_icon = (variation_count > 0) ? '<i class="variation">+</i>' : '';
			
			const preset_args = `{'clothes_id' : '${preset}', 'swatch_id' : '${swatch_id}', 'colors' : '${temp_char.colors}', 'variation' : ${variation_options}, 'print_clothes' : '${clothes_id}'}`;
			
			const preset_class = (clothes_id == preset) ? 'preset active' : 'preset';
			choose_presets += `<button class="${preset_class}" id="${preset}" data-id="${preset}" 
			onclick="print_to_menu('${category}', ${preset_args});"><svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="0 0 1000 1415">${get_svg_code(graphics[preset], temp_char.colors, preset, true)}</svg><label>${graphics[preset].label}</label>${plus_icon}</button>`;
		}
	});
	
	return choose_presets;
}
function print_variation(args){
	
	const clothes_id = args.clothes_id;
	const variation = ( args.hasOwnProperty('variation')) ? args.variation : [0,0,0,0,0,0,0];
	const swatch_id = args.swatch_id;
	let variation_count = 0;
	
	if(args.hasOwnProperty('face')){
		Object.keys(args.face).forEach(function(section_id){
			const section = args.face[section_id];
			temp_char.face[section_id] = section;
		});
	}
	
	let choose_variations =``;
	if(Object.keys(graphics[clothes_id].clothes)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].clothes).length > 1){
		variation_count++;
		choose_variations += `<div class="variation_holder variation_clothes"><label>Clothes</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].clothes).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].clothes)[i];
			const variation_obj = graphics[clothes_id].clothes[variation_name];
			
			if(temp_char.clothes.clothes_v == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${i},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${variation[5]},${variation[6]}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	if(graphics[clothes_id].hasOwnProperty('head') && Object.keys(graphics[clothes_id].head)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].head).length > 1){
		variation_count++;
		choose_variations += `<div class="variation_holder variation_head"><label>Face</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].head).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].head)[i];
			const variation_obj = graphics[clothes_id].head[variation_name];
			
			if(temp_char.body.head_v == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${i},${variation[3]},${variation[4]},${variation[5]},${variation[6]}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	
	if(graphics[clothes_id].hasOwnProperty('hair_front') && Object.keys(graphics[clothes_id].hair_front)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].hair_front).length > 1){
		variation_count++;
		choose_variations += `<div class="variation_holder variation_hair"><label>Hair</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].hair_front).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].hair_front)[i];
			const variation_obj = graphics[clothes_id].hair_front[variation_name];
			
			if(temp_char.body.hair_v == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${variation[2]},${i},${variation[4]},${variation[5]},${variation[6]}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	
	if(graphics[clothes_id].hasOwnProperty('accessory') && Object.keys(graphics[clothes_id].accessory)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].accessory).length > 1){
		variation_count++;
		const acc_label = 'Accessory';
		choose_variations += `<div class="variation_holder variation_acc"><label>${acc_label}</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].accessory).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].accessory)[i];
			const variation_obj = graphics[clothes_id].accessory[variation_name];
			
			if(temp_char.body.acc == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${i},${variation[5]},${variation[6]}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	
	if(graphics[clothes_id].hasOwnProperty('pet') && Object.keys(graphics[clothes_id].pet)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].pet).length > 1){
		variation_count++;
		const acc_label = 'Pet';
		choose_variations += `<div class="variation_holder variation_pet"><label>${acc_label}</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].pet).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].pet)[i];
			const variation_obj = graphics[clothes_id].pet[variation_name];
			
			if(temp_char.body.pet == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${i},${variation[6]}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	
	if(graphics[clothes_id].hasOwnProperty('overtop') && Object.keys(graphics[clothes_id].overtop)[0].startsWith('ver_') && Object.keys(graphics[clothes_id].overtop).length > 1){
		variation_count++;
		const acc_label = 'Over Clothes';
		choose_variations += `<div class="variation_holder variation_overtop"><label>${acc_label}</label>`;
		for(i = 0; i<Object.keys(graphics[clothes_id].overtop).length; i++){
			const variation_name = Object.keys(graphics[clothes_id].overtop)[i];
			const variation_obj = graphics[clothes_id].overtop[variation_name];
			
			if(temp_char.body.overtop == i){
				choose_variations += `<div class="variation current" id="${variation_name}">
					<span>${variation_obj.label}</span>
				</div>`;
			}
			else {
				choose_variations += `<button class="variation" id="${variation_name}" data-id="${variation_name}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${variation[5]},${i}])">
					<span>${variation_obj.label}</span>
				</button>`;
			}
		}
		choose_variations += `</div>`;
	}
	
	
	
	if(graphics[clothes_id].hasOwnProperty('head')) {
		Object.keys(graphics[clothes_id].head).forEach(function(section_id){
			const section = graphics[clothes_id].head[section_id];
			if(Object.keys(section)[0].startsWith('ver_') && Object.keys(section).length > 1){
				variation_count++;
				
				let section_label = section_id;
				if((section_id == 'ears_mid') || (section_id == 'ears_back') || (section_id == 'hair_mid')){
					return;
				}
				if(section_id == 'brows_holder'){
					section_label = 'brows';
				}
				if(section_id == 'base'){
					section_label = 'face';
				}
				choose_variations += `<div class="variation_holder variation_${section_id}"><label>${section_label}</label>`;
				for(i = 0; i<Object.keys(section).length; i++){
					const variation_name = Object.keys(section)[i];
					const variation_obj = section[variation_name];
					
					const default_label = (section_id == 'brows_holder') ? 'brows' + ' ' + i : section_id + ' ' + i;
					const variation_label = (variation_obj.hasOwnProperty('label')) ? variation_obj.label : default_label;
					
					if(temp_char.face[section_id] == i){
						choose_variations += `<div class="variation current" id="${section_id}_${i}">
							<span>${variation_label}</span>
						</div>`;
					}
					else {
						choose_variations += `<button class="variation" id="${section_id}_${i}" data-id="${section_id}_${i}" onclick="main_print('variations', '${clothes_id}', '${swatch_id}', [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${variation[5]},${variation[6]}], {'face' :{'${section_id}' : ${i}}})">
							<span>${variation_label}</span>
						</button>`;
					}
				}
				choose_variations += `</div>`;
			}
		});
	}
	
	
	
	
	const sub_variation_btn = document.getElementById('sub_variations');
	if(sub_variation_btn){
		if(variation_count<=0){
			sub_variation_btn.setAttribute('disabled', "");
		}
		else{
			sub_variation_btn.removeAttribute('disabled');
		}
	}
	
	return choose_variations;
}


function get_categories(args){
	
	const clothes_id = args.clothes_id;
	const swatch_id = args.swatch_id;
	const variation = args.variation;
	
	let categories = [];
	let categories_list = '';
	
	const cur_cat = graphics[clothes_id].category;
	
	Object.keys(graphics).forEach(function(item){
		const the_cat = graphics[item].category;
		if(!categories.includes(the_cat)){
			categories.push(the_cat);
		}
	});
	categories.forEach(function(cat_name){
		categories_list+= `<button value="${cat_name}" onclick="print_to_menu('${cat_name}', {'clothes_id' : '${clothes_id}', 'swatch_id' : '${swatch_id}', 'variation' : [${variation}]})">${cat_name}</button>`;
		
	});
	
	return categories_list;
}

function get_preset_sections(object_obj){
	
	
	let keys_holder = [];
	
	Object.keys(object_obj).forEach(function(section_id){
		
		if( (section_id == 'dpath') || (section_id == 'eye_white') || (section_id == 'label') || (section_id == 'category') || (section_id == 'crop')){
			return;
		}
		keys_holder.push(section_id);
		
		const the_section = object_obj[section_id];
		
		if( Object.prototype.toString.call( the_section ) === '[object Object]' ){
			const additional = get_preset_sections(the_section);
			additional.forEach(function(ind){
				if((ind != 'dpath') && !keys_holder.includes(ind)){
					keys_holder.push(ind);
				}
				
			});
		}
	});
	
	return keys_holder;
}

function get_color_pickers(args){
	
	const clothes_id = args.clothes_id;
	const swatch_id = args.swatch_id;
	const variation = args.variation;
	
	const preset_sections = get_preset_sections(graphics[clothes_id]); 
	console.log('sec: ' + preset_sections.includes('sec'));
	console.log('purple: ' + preset_sections.includes('purple'));
	
	let choose_colors =``;
	Object.keys(swatches[swatch_id].values).forEach(function(color_option){
		if(color_option == 'face'){
			Object.keys(swatches[swatch_id].values.face).forEach(function(face_color_option){
				if(!preset_sections.includes(face_color_option)){
					return;
				}
				choose_colors += `<div class="color_box">
					<label for="picker_${face_color_option}">${face_color_option}</label>
					<input id="picker_${face_color_option}" onchange="update_color('${face_color_option}', 'colors', this, [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${variation[5]},${variation[6]}])" value="#${swatches[swatch_id].values.face[face_color_option]}" type="color" title="${face_color_option}" />
				</div>`;
			});
		}
		else if(color_option != 'acc_path'){
			if(!preset_sections.includes(color_option)){
				return;
			}
			choose_colors += `<div class="color_box">
					<label for="picker_${color_option}">${color_option}</label>
					<input id="picker_${color_option}" onchange="update_color('${color_option}', 'colors', this, [${variation[0]},${variation[1]},${variation[2]},${variation[3]},${variation[4]},${variation[5]},${variation[6]}])" value="#${swatches[swatch_id].values[color_option]}" type="color" title="${color_option}" />
				</div>`;
		}
	});
	
	return choose_colors;
}
function get_color_swatches(args){
	
	const clothes_id = args.clothes_id;
	const swatch_id = args.swatch_id;
	const variation = args.variation;
	
	let choose_swatches =``;
	Object.keys(swatches).forEach(function(swatch){
		if(swatch != 'white' && swatch != 'brown'){
			choose_swatches += `<button class="swatch" id="${swatch}" data-id="${swatch}" onclick="main_print('colors', '${clothes_id}', '${swatch}', [${variation}])">
				<span>${swatches[swatch].label}</span>
				<div class="swatch_gradient" style="background:linear-gradient(90deg, #${swatches[swatch].values.skin} 0%, #${swatches[swatch].values.skin} 25%, #${swatches[swatch].values.main} 25%, #${swatches[swatch].values.main} 50%, #${swatches[swatch].values.sec} 50%, #${swatches[swatch].values.sec} 75%, #${swatches[swatch].values.trim} 75%, #${swatches[swatch].values.trim} 100%);"></div>
			</button>`;
		}
		
	});
	
	return choose_swatches;
}

function print_to_menu(category_name = 'neutral', cat_args){
	
	if(cat_args.hasOwnProperty('clothes_id')){
		const preset_id = cat_args.clothes_id;
		temp_char.body.body = Object.keys(graphics).indexOf(preset_id);
	}
	
	document.getElementById('category').innerHTML = print_by_cat(category_name, cat_args);
	document.getElementById('variations_list').innerHTML = print_variation(cat_args);
	document.getElementById('category_list').innerHTML = get_categories(cat_args);
	document.getElementById('swatches_list').innerHTML = get_color_swatches(cat_args);
	document.getElementById('input_holder').innerHTML = get_color_pickers(cat_args);
	print_portrait(cat_args.clothes_id, temp_char.colors, cat_args.print_clothes);
	
	document.querySelector(`button[value="${category_name}"]`).classList = 'current';
}

function change_file_type(){
	const filetype_select = document.getElementById('file_type');
	const export_btn = document.getElementById('export_btn');
	
	const file_type = filetype_select.value;
	
	export_btn.setAttribute('onclick',`save_character_image('${file_type}')`);
	export_btn.innerHTML = `Export ${file_type.toUpperCase()}`;
}

function change_crop_type(){
	const crop_select = document.getElementById('crop');
	const export_btn = document.getElementById('export_btn');
	
	const crop_value = crop_select.value;
	
	temp_char.crop = crop_value;
	
	const image_width_inp = document.getElementById('image_width');
	const image_height_span = document.getElementById('image_height');
	
	if(crop_value == 'closeup'){
		image_width_inp.value = 400;
		image_height_span.innerHTML = 300;
		image_width_inp.setAttribute('min', '400');
		image_width_inp.setAttribute('value', '400');
		image_width_inp.setAttribute('max', '800');
	}
	else{
		image_width_inp.value = 1000;
		image_height_span.innerHTML = 1415;
		image_width_inp.setAttribute('min', '1000');
		image_width_inp.setAttribute('value', '1000');
		image_width_inp.setAttribute('max', '4000');
	}
	
	
	
	clothes_id = Object.keys(graphics)[temp_char.body.body];
	print_portrait(graphics[clothes_id], temp_char.colors, clothes_id);
}

function change_image_width(){
	const image_width_inp = document.getElementById('image_width');
	const image_height_span = document.getElementById('image_height');
	
	let image_width = image_width_inp.value;
	
	if(temp_char.crop == 'closeup'){
		if(image_width<400){
			image_width = 400;
		} else if(image_width>800){
			image_width = 800;
		}
		image_width_inp.value = image_width;
		image_height_span.innerHTML = Math.floor(image_width/400*300);
	}
	else{
		if(image_width<1000){
			image_width = 1000;
		} else if(image_width>4000){
			image_width = 4000;
		}
		image_width_inp.value = image_width;
		image_height_span.innerHTML = Math.floor(image_width/1000*1415);
	}
	
	clothes_id = Object.keys(graphics)[temp_char.body.body];
	print_portrait(graphics[clothes_id], temp_char.colors, clothes_id);
}

function print_export_options(){
	let the_html = '';
	
	const crop = temp_char.crop;
	const width = (crop == 'closeup') ? [400, 800, 400] : [1000, 4000, 1000];
	const height = (crop == 'closeup') ? Math.floor(width[2]/400*300) : Math.floor(width[2]/1000*1415);
	
	
	the_html += `<label for="crop">Crop Image</label>
	<select name="crop" id="crop" onchange="change_crop_type();">
		<option value="full" ${(crop == 'full') ? 'selected' : ''}>Full</option>
		<option value="vn" ${(crop == 'vn') ? 'selected' : ''}>Visual Novel</option>
		<option value="closeup" ${(crop == 'closeup') ? 'selected' : ''}>Closeup</option>
	</select>
	<label for="file_type">Choose File Type</label>
	<select name="file_type" id="file_type" onchange="change_file_type();">
		<option value="svg">SVG</option>
		<option value="png">PNG</option>
		<option value="webp">WEBP</option>
	</select>
	<label for="image_width">Choose Image Size</label>
	<input id="image_width" type="number" min="${width[0]}" max="${width[1]}" value="${width[2]}" onchange="change_image_width();" />
	<span id="image_height">${height}</span>`;	
	
	return the_html;
}

function main_print(sub_menu = 'presets', clothes_id = false, swatch_id = (swatches.hasOwnProperty('custom')) ? 'custom' : 'default', variation = [0,0,0,0,0,0,0], args = false){
	
	temp_char.clothes.clothes_v = variation[0];
	temp_char.body.body_v = variation[1];
	temp_char.body.head_v = variation[2];
	temp_char.body.hair_v = variation[3];
	temp_char.body.acc = variation[4];
	temp_char.body.pet = variation[5];
	temp_char.body.overtop = variation[6];
	
	if(args.hasOwnProperty('face')){
		Object.keys(args.face).forEach(function(section_id){
			if(temp_char.face.hasOwnProperty(section_id)){
				temp_char.face[section_id] = args.face[section_id];
			}
		});
	}
	
	
	temp_char.colors = swatch_id;
	
	const crop_type = (args && args.hasOwnProperty('crop')) ? args.crop : temp_char.crop;
	temp_char.crop = crop_type;
	
	if(clothes_id){
		temp_char.body.body = Object.keys(graphics).indexOf(clothes_id);
	} 
	else {
		clothes_id = Object.keys(graphics)[temp_char.body.body];
	}
	
	
	const graphic_info = graphics[clothes_id];
	
	const cat_id = graphic_info.category;
	
	const print_to = document.getElementById('viewport');
	
	
	let choose_presets = print_by_cat(cat_id, {'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	
	let choose_swatches = get_color_swatches({'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	
	
	let choose_colors = get_color_pickers({'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	
	let choose_variations = print_variation({'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	
	let categories_list = get_categories({'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	
	let export_choices = print_export_options();
	
	
	
	
	const menu_html = `<div id="main_menu" class="${sub_menu}">
		<div id="choose_submenu">
			<button onclick="change_parent_class('presets', this)" id="sub_presets">Presets</button>
			<button onclick="change_parent_class('variations', this)" id="sub_variations">Variations</button>
			<button onclick="change_parent_class('colors', this)" id="sub_colors">Colors</button>
			<button onclick="change_parent_class('export', this)" id="sub_export">Export</button>
		</div>
		<div id="presets">
			<h2>Choose Preset</h2>
			<div id="category_list">${categories_list}</div>
			<div id="category">${choose_presets}</div>
		</div>
		<div id="variations">
			<h2>Choose Variation</h2>
			<div id="variations_list">
				${choose_variations}
			</div>
		</div>
		<div id="colors">
			<div id="swatches_holder">
				<h2>Choose Color Swatch</h2>
				<div id="swatches_list">
					${choose_swatches}
				</div>
			</div>
			<div id="colors_holder">
				<h2>Choose Colors</h2>
				<div id="input_holder">${choose_colors}</div>
			</div>
		</div>
		<div id="export_buttons">
			<h2>Export Portrait</h2>
			${export_choices}
			<button id="export_btn" onclick="save_character_image('svg');">Export SVG</button>
		</div>
	</div>`;
	
	
	
	
	stamp_d ='';
	
	
	const viewbox = (graphics[clothes_id].hasOwnProperty('crop') && graphics[clothes_id].crop.hasOwnProperty(temp_char.crop)) ? graphics[clothes_id].crop[temp_char.crop] : default_crop[temp_char.crop];
	const img_sizes = (temp_char.crop == 'closeup') ? 'width="400" height="300"' : '';
	const aspect_ratio = (temp_char.crop == 'closeup') ? 'style="aspect-ratio:400/300;"' : 'style="aspect-ratio:1000/1415;"';
	
	
	const portrait_html = `<canvas id="hidden_canvas" width="1000" height="1415"></canvas>
	<div id="linkholder"></div>
	<svg id="main_portrait" xmlns="http://www.w3.org/2000/svg" xml:space="preserve" viewBox="${viewbox}" preserveAspectRatio="xMidYMin slice" ${img_sizes} ${aspect_ratio}></svg>`;
		
	
	
	
	print_to.innerHTML = menu_html + portrait_html;
	
	print_to_menu(cat_id, {'clothes_id' : clothes_id, 'swatch_id' : swatch_id, 'variation' : variation});
	//print_portrait(graphic_info, temp_char.colors, clothes_id);
}

function print_portrait(graphics_obj, swatch, print_clothes = false){
	if((typeof graphics_obj === 'string') || (graphics_obj instanceof String)){
		graphics_obj = graphics[graphics_obj];
	}
	const notes = `<desc>${Notes}</desc>`;

	const portrait_print = get_svg_code(graphics_obj, swatch, print_clothes);
	const stamp_full = '';//get_svg_code(graphics_obj, 'white', print_clothes);
	const stamp_full_brown = '';//get_svg_code(graphics_obj, 'brown', print_clothes);
	
	let the_html = `${notes} ${stamp_full} ${stamp_full_brown} ${portrait_print}`;
	
	
	const viewbox = (graphics_obj.hasOwnProperty('crop') && graphics_obj.crop.hasOwnProperty(temp_char.crop)) ? graphics_obj.crop[temp_char.crop] : default_crop[temp_char.crop];
	let view_style = (temp_char.crop == 'closeup') ? 'aspect-ratio:400/300;' : 'aspect-ratio:1000/1415;';
	
	document.getElementById('main_portrait').setAttribute('viewBox', viewbox);
	if(temp_char.crop == 'closeup'){
		const view_width = 800;//document.getElementById('image_width').value;
		document.getElementById('main_portrait').setAttribute('width', view_width);
		document.getElementById('main_portrait').setAttribute('height', Math.floor(view_width/400*300));
		view_style += 'max-height:' + Math.floor(view_width/400*300) + 'px;';
	}
	else{
		const view_width = 1000;//document.getElementById('image_width').value;
		document.getElementById('main_portrait').setAttribute('width', view_width);
		document.getElementById('main_portrait').setAttribute('height', Math.floor(view_width/1000*1415));
		view_style += 'max-height:' + Math.floor(view_width/1000*1415) + 'px; max-width:fit-content;';
	}
	document.getElementById('main_portrait').setAttribute('style', view_style);
	
	//console.log(document.getElementById('main_portrait').getAttribute('viewBox'));
	
	document.getElementById('main_portrait').innerHTML = the_html;
}

function get_svg_code(obj, print_in_white = 'default', clothes_type = false, limited = false){
	/*
	const graphic_info = graphics['default'];
	if(clothes_type && graphic_info.clothes.hasOwnProperty(clothes_type)){
		temp_char.clothes[graphic_info.clothes[clothes_type].type] = clothes_type;
	}
	*/
	let portrait_print ='';
	let fill_color = '';
	if(!obj || obj==undefined){return}
	
	Object.keys(obj).forEach(function(info){
		
		let opacity = '1';
		
		const stroke_width = (print_in_white == 'white') ? 'stroke-width="5" stroke="#ffffff" stroke-linejoin="round"' : ((print_in_white == 'brown') ? 'stroke-width="3" stroke="#a9a9a9" stroke-linejoin="round"' : '');
		
		if((info == 'label') || (info == 'category') || (info == 'type') || (info == 'crop')){
			return;
		}
		else if(info == 'defs'){
			portrait_print += obj[info];
		}
		else if(info == 'path'){
			fill_color = (print_in_white == 'white') ? '#ffffff' : 'url(#acc_grad)';
			portrait_print += `<path class="${info}" fill="${fill_color}" d="${obj[info]}" opacity="${opacity}" />`;
			stamp_d += obj[info];
		}
		else {
			let fill_value = '000000';
			
			if( swatches[print_in_white].values.face.hasOwnProperty(info) ) {
				fill_value = swatches[print_in_white].values.face[info];
			} else if (swatches[print_in_white].values.hasOwnProperty(info)) {
				fill_value = swatches[print_in_white].values[info];
			} else if (swatches['default'].values.hasOwnProperty(info)) {
				fill_value = swatches['default'].values[info];
			}
			
			fill_color = '#' + fill_value;
			if(info == 'dpath'){
				fill_color = 'inherit';
			}
			else if(info == 'lines'){
				fill_color = '#000000';
			}
			else if(print_in_white == 'white'){
				fill_color = '#ffffff';
			}
			else if((info == 'fill_light') || (info == 'rim_light')){
				fill_color = '#00ffff';
				opacity = '0.3';
			}
			else if((info == 'shadow') || (info == 'shadows')){
				fill_color = '#000000';
				opacity = '0.3';
			}
			else if((info == 'light') || (info == 'lights')){
				fill_color = '#ffffff';
				opacity = '0.3';
			}
			else if(info == 'opacity'){
				fill_color = 'inherit';
				opacity = '0.3';
			}
			
			if( Object.prototype.toString.call( obj[info] ) === '[object Object]' ){
				
				const obj_children = Object.keys(obj[info]);
				
				if(info == 'clothes') {
					const clothes_v = ((obj_children.length>temp_char.clothes.clothes_v) && obj_children[temp_char.clothes.clothes_v].startsWith('ver_')) ? obj_children[temp_char.clothes.clothes_v] : false; 
					const to_print = (clothes_v && obj[info].hasOwnProperty(clothes_v)) ? obj[info][clothes_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				} 
				else if(info == 'body'){
					const body_v = ((obj_children.length>temp_char.body.body_v) && obj_children[temp_char.body.body_v].startsWith('ver_')) ? obj_children[temp_char.body.body_v] : false; 
					const to_print = (body_v && obj[info].hasOwnProperty(body_v)) ? obj[info][body_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				} 
				else if((info == 'head')){
					const head_v = ((obj_children.length>temp_char.body.head_v) && obj_children[temp_char.body.head_v].startsWith('ver_')) ? obj_children[temp_char.body.head_v] : false; 
					const to_print = (head_v && obj[info].hasOwnProperty(head_v)) ? obj[info][head_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				}
				else if((info == 'hair_back') || (info == 'hair_mid') || (info == 'hair_front') || (info == 'hair_holder')){
					
					const hair_v = ((obj_children.length>temp_char.body.hair_v) && obj_children[temp_char.body.hair_v].startsWith('ver_')) ? obj_children[temp_char.body.hair_v] : false; 
					const to_print = (hair_v && obj[info].hasOwnProperty(hair_v)) ? obj[info][hair_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
					
				}
				else if((info == 'ears_back') || (info == 'ears_mid') || (info == 'ears_front') || (info == 'ears')){
					
					const ears_id = ((obj_children.length>temp_char.face.ears) && obj_children[temp_char.face.ears].startsWith('ver_')) ? obj_children[temp_char.face.ears] : false; 
					const to_print = (ears_id && obj[info].hasOwnProperty(ears_id)) ? obj[info][ears_id] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
					
				}
				else if((info == 'overtop') || (info == 'overtop_back') ){
					const overtop_v = ((obj_children.length>temp_char.body.overtop) && obj_children[temp_char.body.overtop].startsWith('ver_')) ? obj_children[temp_char.body.overtop] : false; 
					const to_print = (overtop_v && obj[info].hasOwnProperty(overtop_v)) ? obj[info][overtop_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				}
				else if((info == 'accessory') || info.includes('accessory')){
					const acc_v = ((obj_children.length>temp_char.body.acc) && obj_children[temp_char.body.acc].startsWith('ver_')) ? obj_children[temp_char.body.acc] : false; 
					const to_print = (acc_v && obj[info].hasOwnProperty(acc_v)) ? obj[info][acc_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				}
				else if((info == 'pet') || (info == 'pet_back')){
					const pet_v = ((obj_children.length>temp_char.body.pet) && obj_children[temp_char.body.pet].startsWith('ver_')) ? obj_children[temp_char.body.pet] : false; 
					const to_print = (pet_v && obj[info].hasOwnProperty(pet_v)) ? obj[info][pet_v] : obj[info];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(to_print, print_in_white, clothes_type, limited)}</g>`;
				}
				else if(temp_char['body'].hasOwnProperty(info)){
					const print_type = obj_children[temp_char['body'][info]];
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(obj[info][print_type], print_in_white, clothes_type, limited)}</g>`;
				}
				else if(temp_char['face'].hasOwnProperty(info) && obj_children[0] && obj_children[0].startsWith('ver_')){
					const ver_index = (temp_char['face'][info]<obj_children.length) ? temp_char['face'][info] : obj_children.length-1;
					const print_type = obj_children[ver_index];
					
					
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(obj[info][print_type], print_in_white, clothes_type, limited)}</g>`;
				}
				else {
					portrait_print += `<g class="${info}" fill="${fill_color}" ${stroke_width} opacity="${opacity}">${get_svg_code(obj[info], print_in_white, clothes_type, limited)}</g>`;
				}
			}
			else{
				portrait_print += `<path class="${info}" fill="${fill_color}" d="${obj[info]}" opacity="${opacity}" ${stroke_width} />`;
				stamp_d += obj[info];
			}
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
	
	const preset_name = Object.keys(graphics)[temp_char.body.body];
	
	const crop_type = document.getElementById('crop').value;
	const image_width = document.getElementById('image_width').value;
	const image_height = (crop_type == 'closeup') ? Math.floor(image_width/400*300) : Math.floor(image_width/1000*1415);
	
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
	else{
		
		const compression = {
			'png' : 1.0,
			'jpg' : 0.8,
			'webp' : 0.99,
		}
		
        const uriData = `data:image/svg+xml;base64,${btoa(new XMLSerializer().serializeToString(svgElement))}`
        const img = new Image()
        img.src = uriData
        img.onload = () => {
            const canvas = document.createElement("canvas");
            [canvas.width, canvas.height] = [image_width, image_height]
            const ctx = canvas.getContext("2d")
            ctx.drawImage(img, 0, 0, image_width, image_height)

            // 👇 download
            const a = document.createElement("a")
            a.href = canvas.toDataURL('image/' + filetype, compression[filetype]);
            a.download = `${preset_name}_v${t}.${filetype}`
            a.append(canvas)
            a.click()
            a.remove()
        }
		
	}
}

function update_color(part = false, c_sub_menu, obj, cvariation = [0,0,0,0,0,0,0]){
	//console.log(obj);
	const color_val = obj.value.split('#')[1];
	
	swatches['custom'] = {
		'label' : 'Custom',
		'values' : {
			'skin' 		: '',//((document.getElementById('picker_skin')) ? document.getElementById('picker_skin').value.split('#')[1] : swatches['default'].skin),
			'main' 		: '',//((document.getElementById('picker_main')) ? document.getElementById('picker_main').value.split('#')[1] : swatches['default'].main),
			'sec' 		: '',//((document.getElementById('picker_sec')) ? document.getElementById('picker_sec').value.split('#')[1] : swatches['default'].sec),
			'trim' 		: '',//((document.getElementById('picker_trim')) ? document.getElementById('picker_trim').value.split('#')[1] : swatches['default'].trim),
			'hair'		: '',//((document.getElementById('picker_hair')) ? document.getElementById('picker_hair').value.split('#')[1] : swatches['default'].hair),
			'brows'		: '',//((document.getElementById('picker_brows')) ? document.getElementById('picker_brows').value.split('#')[1] : swatches['default'].brows),
			'face' 		: {
				'eye_white' 	: '',//((document.getElementById('picker_eye_white')) ? document.getElementById('picker_eye_white').value.split('#')[1] : swatches['default'].face.eye_white),
				'eye_color' 	: '',//((document.getElementById('picker_eye_color')) ? document.getElementById('picker_eye_color').value.split('#')[1] : swatches['default'].face.eye_color),
				'lips' 		: '',//((document.getElementById('picker_lips')) ? document.getElementById('picker_lips').value.split('#')[1] : swatches['default'].face.lips),
				'teeth' 	: '',//((document.getElementById('picker_teeth')) ? document.getElementById('picker_teeth').value.split('#')[1] : swatches['default'].face.teeth),
			},
			'green' 	: '',//((document.getElementById('picker_green')) ? document.getElementById('picker_green').value.split('#')[1] : swatches['default'].green),
			'orange'	: '',//((document.getElementById('picker_orange')) ? document.getElementById('picker_orange').value.split('#')[1] : swatches['default'].orange),
			'lyrics'	: '',//((document.getElementById('picker_lyrics')) ? document.getElementById('picker_lyrics').value.split('#')[1] : swatches['default'].lyrics),
			'yellow'	: '',//((document.getElementById('picker_yellow')) ? document.getElementById('picker_yellow').value.split('#')[1] : swatches['default'].yellow),
			'purple' 	: '',//((document.getElementById('picker_purple')) ? document.getElementById('picker_purple').value.split('#')[1] : swatches['default'].purple),
			'white' 	: '',//((document.getElementById('picker_white')) ? document.getElementById('picker_white').value.split('#')[1] : swatches['default'].white),
			'metal' 	: '',//((document.getElementById('picker_metal')) ? document.getElementById('picker_metal').value.split('#')[1] : swatches['default'].metal),
			'dmetal'	: '',//((document.getElementById('picker_dmetal')) ? document.getElementById('picker_dmetal').value.split('#')[1] : swatches['default'].dmetal),
			'nails' 	: '',//((document.getElementById('picker_nails')) ? document.getElementById('picker_nails').value.split('#')[1] : swatches['default'].nails),
			'palm' 		: '',//((document.getElementById('picker_palm')) ? document.getElementById('picker_palm').value.split('#')[1] : swatches['default'].palm),
			'acc_path' 	: 'acc_grad',
		},
	};
	
	Object.keys(swatches['default'].values).forEach(function(type){
		if(type == 'face'){
			Object.keys(swatches['default'].values.face).forEach(function(f_type){
				const f_picker = document.getElementById('picker_' + f_type);
				const default_value = swatches['default'].values.face[f_type];
				
				if(f_picker != null){
					swatches['custom'].values.face[f_type] = f_picker.value.split('#')[1];
				}
				else{
					swatches['custom'].values.face[f_type] = default_value;
				}
			});
		}
		else{
			const picker = document.getElementById('picker_' + type);
			const default_value = swatches['default'].values[type];
			if(picker != null){
				swatches['custom'].values[type] = picker.value.split('#')[1];
			}
			else{
				swatches['custom'].values[type] = default_value;
			}
		}
		
	});
	
		
	/*
	if(swatches.custom.values.hasOwnProperty(part)){
		swatches.custom.values[part] = color_val;
	}
	if(swatches.custom.values.face.hasOwnProperty(part)){
		swatches.custom.values.face[part] = color_val;
	}
	*/
	main_print(c_sub_menu, false, 'custom', cvariation);
	//print_portrait(graphics['default'], 'custom', c_cur_id);
}


function update_feature(part = false, color_swatch = 'default', the_clothes = temp_char.preset, obj){	
	
	temp_char.body[part] = obj.value;
	
	print_portrait(graphics['default'], color_swatch, the_clothes);
}