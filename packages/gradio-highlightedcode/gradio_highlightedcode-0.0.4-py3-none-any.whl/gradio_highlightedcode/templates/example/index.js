const {
  SvelteComponent: f,
  append_hydration: u,
  attr: d,
  children: o,
  claim_element: h,
  claim_text: g,
  detach: _,
  element: m,
  init: y,
  insert_hydration: v,
  noop: c,
  safe_not_equal: b,
  set_data: E,
  text: q,
  toggle_class: r
} = window.__gradio__svelte__internal;
function w(n) {
  let e, a = (
    /*value*/
    (n[0] ? (
      /*value*/
      n[0]
    ) : "") + ""
  ), s;
  return {
    c() {
      e = m("pre"), s = q(a), this.h();
    },
    l(t) {
      e = h(t, "PRE", { class: !0 });
      var l = o(e);
      s = g(l, a), l.forEach(_), this.h();
    },
    h() {
      d(e, "class", "svelte-1ioyqn2"), r(
        e,
        "table",
        /*type*/
        n[1] === "table"
      ), r(
        e,
        "gallery",
        /*type*/
        n[1] === "gallery"
      ), r(
        e,
        "selected",
        /*selected*/
        n[2]
      );
    },
    m(t, l) {
      v(t, e, l), u(e, s);
    },
    p(t, [l]) {
      l & /*value*/
      1 && a !== (a = /*value*/
      (t[0] ? (
        /*value*/
        t[0]
      ) : "") + "") && E(s, a), l & /*type*/
      2 && r(
        e,
        "table",
        /*type*/
        t[1] === "table"
      ), l & /*type*/
      2 && r(
        e,
        "gallery",
        /*type*/
        t[1] === "gallery"
      ), l & /*selected*/
      4 && r(
        e,
        "selected",
        /*selected*/
        t[2]
      );
    },
    i: c,
    o: c,
    d(t) {
      t && _(e);
    }
  };
}
function p(n, e, a) {
  let { value: s } = e, { type: t } = e, { selected: l = !1 } = e;
  return n.$$set = (i) => {
    "value" in i && a(0, s = i.value), "type" in i && a(1, t = i.type), "selected" in i && a(2, l = i.selected);
  }, [s, t, l];
}
class C extends f {
  constructor(e) {
    super(), y(this, e, p, w, b, { value: 0, type: 1, selected: 2 });
  }
}
export {
  C as default
};
