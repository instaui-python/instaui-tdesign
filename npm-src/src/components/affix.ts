import type { AffixProps } from "tdesign-vue-next";
import type { SetupContext } from "vue";

export function withDefaultContainer(attrs: SetupContext["attrs"]): AffixProps["container"] {
  const { container = ".insta-main" } = attrs as AffixProps;

  return container;
}
