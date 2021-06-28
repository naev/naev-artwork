RES_TINY := $(if $(HIDPI),48,24)
RES_SMALL := $(if $(HIDPI),128,64)
OUTDIR := ../../out/logo
TINY_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%_tiny.png,$(wildcard *.svg))
SMALL_OUTPUTS := $(patsubst %.svg,$(OUTDIR)/%_small.png,$(wildcard *.svg))
OUTPUTS := $(TINY_OUTPUTS) $(SMALL_OUTPUTS)

all: $(OUTPUTS)
clean:
	rm -f $(OUTPUTS)

$(OUTDIR):
	mkdir -p $@

$(OUTDIR)/%_tiny.png: %.svg | $(OUTDIR)
	python export.py "$<" $(RES_TINY) "$@"

$(OUTDIR)/%_small.png: %.svg | $(OUTDIR)
	python export.py "$<" $(RES_SMALL) "$@"

.PHONY: all clean
