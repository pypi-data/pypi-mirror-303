import{j as e}from"./reactflow-vendor-DVEEOIVt.js";import{c as o,f as h,S as f,F as u,B as j}from"./shallow-Djyvgrt4.js";import{C as v}from"./CustomDrawer-NgkiQ4p9.js";import{r as l}from"./react-vendor-4ldeB94U.js";import{l as g}from"./index-CjkvpB-0.js";import{S as c}from"./Stack-D0KwXe3b.js";import{I as y}from"./IconFolder-DighP31t.js";/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var k=o("outline","box","IconBox",[["path",{d:"M12 3l8 4.5l0 9l-8 4.5l-8 -4.5l0 -9l8 -4.5",key:"svg-0"}],["path",{d:"M12 12l8 -4.5",key:"svg-1"}],["path",{d:"M12 12l0 9",key:"svg-2"}],["path",{d:"M12 12l-8 -4.5",key:"svg-3"}]]);/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var N=o("outline","brand-tabler","IconBrandTabler",[["path",{d:"M8 9l3 3l-3 3",key:"svg-0"}],["path",{d:"M13 15l3 0",key:"svg-1"}],["path",{d:"M4 4m0 4a4 4 0 0 1 4 -4h8a4 4 0 0 1 4 4v8a4 4 0 0 1 -4 4h-8a4 4 0 0 1 -4 -4z",key:"svg-2"}]]);/**
 * @license @tabler/icons-react v3.18.0 - MIT
 *
 * This source code is licensed under the MIT license.
 * See the LICENSE file in the root directory of this source tree.
 */var I=o("filled","triangle-inverted-filled","IconTriangleInvertedFilled",[["path",{d:"M20.118 3h-16.225a2.914 2.914 0 0 0 -2.503 4.371l8.116 13.549a2.917 2.917 0 0 0 4.987 .005l8.11 -13.539a2.914 2.914 0 0 0 -2.486 -4.386z",key:"svg-0"}]]);function d({path:t}){const[a,n]=l.useState([]),{setDropingNode:m}=g(),[x,i]=l.useState(!1);return l.useEffect(()=>{i(!0),h("/list_package_children?path="+encodeURIComponent(t)).then(s=>s.json()).then(s=>{n(s)}).finally(()=>{i(!1)})},[]),e.jsx("div",{className:"flex flex-col",children:e.jsxs("div",{className:"flex flex-col",children:[x&&e.jsx(f,{}),a.map(s=>{var p;return s.type==="folder"?e.jsx(b,{node:s},s.path):e.jsxs(c,{onClick:()=>{},children:[e.jsx(u,{children:e.jsx("p",{className:"text-muted-foreground",children:s.name})}),(p=s.functions)==null?void 0:p.map(r=>e.jsxs("div",{draggable:!0,onDragStart:F=>{console.log(r),m(r)},className:"flex flex-row items-center ml-2 py-1 font-semibold gap-1 cursor-pointer hover:bg-secondary",children:[e.jsx(N,{size:18}),e.jsx("span",{children:r.name})]},s.path+"_"+r.name))]},s.type+"_"+s.name)})]})})}function b({node:t}){const[a,n]=l.useState(!1);return e.jsxs(c,{className:"",children:[e.jsxs("div",{className:"flex flex-row items-center cursor-pointer",onClick:()=>n(!a),children:[e.jsx(I,{size:8,className:a?"mr-1":"-rotate-90 mr-1"}),e.jsx(y,{className:"mr-1"}),t.name]}),a&&e.jsx("div",{className:"ml-3",children:e.jsx(d,{path:t.path})})]})}function T(){const[t,a]=l.useState(!1);return e.jsxs(e.Fragment,{children:[e.jsx(j,{onClick:()=>a(!0),left:e.jsx(k,{size:18}),children:"Nodes"}),t&&e.jsx(v,{onClose:()=>a(!1),backdrop:null,children:e.jsxs(c,{className:"w-[400px] py-2 px-2 overflow-y-auto h-[100vh]",children:[e.jsx("h2",{className:"text-xl font-bold p-2",children:"Nodes"}),e.jsx(d,{path:""})]})})]})}export{T as default};
