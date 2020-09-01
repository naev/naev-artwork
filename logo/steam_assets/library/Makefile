OUTDIR := ../../out/steam
OUTPUTS := $(patsubst %.xcf,$(OUTDIR)/%.png,$(wildcard *.xcf))

all: library capsule

library: $(OUTPUTS)
$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%.png: %.xcf | $(OUTDIR)
	../gimp_export.sh -f "$<" -o "$@"

capsule:
	$(MAKE) -C capsule

.PHONY: library capsule
