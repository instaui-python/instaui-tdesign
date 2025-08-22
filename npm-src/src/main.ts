import { type App } from "vue";
import TDesign from "tdesign-vue-next";
import Table from "@/components/Table.vue";
import "./style/index.css";

function install(app: App) {
  app.use(TDesign);
  app.component("t-table", Table);
}

export { install };
