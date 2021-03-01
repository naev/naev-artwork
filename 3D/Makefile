

RENDER      := "./render.py"
RENDER_COMM := "./render_comm.py"
MKSPR       := "./mkspr"

SPRITE_OBJS := $(patsubst %.blend,raw/%.png,$(wildcard ships/*.blend))
COMM_OBJS   := $(patsubst %.blend,raw/%_comm.png,$(wildcard ships/*.blend))

.PHONY: all comm sprite

all: comm sprite

raw/%.png: %.blend mkspr
	@echo -n "Rendering $< ... "
	@blender "$<" -P $(RENDER) > /dev/null
	@$(MKSPR)
	@cp "sprite.png"  "$@"
	@echo "done!"
	@rm *.png

raw/%_comm.png: %.blend
	@echo -n "Rendering $< ... "
	@blender "$<" -P $(RENDER_COMM) > /dev/null
	@cp "comm.png" "$@"
	@echo "comm done!"
	@rm *.png

comm: $(COMM_OBJS)

sprite: $(SPRITE_OBJS)

mkspr: mkspr.c
	$(CC) `pkg-config --cflags --libs SDL2_image libpng` -DNOLOGPRINTFCONSOLE -o "$@" "$<"

clean:
	$(RM) $(COMM_OBJS) $(SPRITE_OBJS) $(MKSPR)

