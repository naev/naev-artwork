

BLENDER     ?= "blender"
RENDER      := "./render.py"
RENDER_COMM := "./render_comm.py"
MKSPR       := "./mkspr"

SPRITE_OBJS := $(patsubst %.blend,raw/%.png,$(wildcard ships/*.blend))
ENGINE_OBJS := $(patsubst %.blend,raw/%_engine.png,$(wildcard ships/*.blend))
COMM_OBJS   := $(patsubst %.blend,raw/%_comm.png,$(wildcard ships/*.blend))

.PHONY: all dirs comm sprite

all: dirs comm sprite engine

dirs:
	@mkdir -p raw/ships

raw/%.png: %.blend mkspr
	@echo -n "Rendering $< ... "
	@$(BLENDER) --background "$<" -P $(RENDER) -x 8 -y 8 > /dev/null
	@$(MKSPR) 8 8
	@cp "sprite.png"  "$@"
	@echo "done!"
	@rm *.png

raw/%_engine.png: %.blend mkspr
	@echo -n "Rendering $< ... "
	@$(BLENDER) --background "$<" -P $(RENDER) -- --engine true -x 8 -y 8 > /dev/null
	@$(MKSPR) 8 8
	@cp "sprite.png"  "$@"
	@echo "done!"
	@rm *.png

raw/%_comm.png: %.blend
	@echo -n "Rendering $< ... "
	@$(BLENDER) --background "$<" -P $(RENDER) -- --comm 1 -x 1 -y 1 -r 255 > /dev/null
	@cp "000.png" "$@"
	@echo "comm done!"
	@rm *.png

comm: $(COMM_OBJS)

sprite: $(SPRITE_OBJS)

engine: $(ENGINE_OBJS)

mkspr: mkspr.c
	$(CC) `pkg-config --cflags --libs SDL2_image libpng` -DNOLOGPRINTFCONSOLE -o "$@" "$<"

clean:
	$(RM) $(COMM_OBJS) $(SPRITE_OBJS) $(MKSPR)

