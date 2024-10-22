import{j as e,x as h,b7 as x,du as b,dv as f,l as n,dw as r,dx as y,dy as P,r as v,t as w,dz as R}from"./vendor-6IcPAw_j.js";import{v as L,a4 as z}from"./vendor-arizeai-DRZuoyuF.js";import{E as k,L as E,R as $,r as j,a as I,F as S,A,b as C,c as F,P as T,h as O,M as D,d,D as B,e as G,f as M,g as N,i as W,j as q,T as H,p as _,k as c,l as J,m as K,n as p,o as Q,q as m,s as g,t as U,v as V,w as X,x as Y,y as Z,z as ee,S as re,B as ae,C as oe,G as te,H as ne,I as se,J as le}from"./pages-CAL1FDMt.js";import{bG as ie,j as de,R as ce,bH as pe,bI as me}from"./components-hX0LgYz3.js";import"./vendor-three-DwGkEfCM.js";import"./vendor-recharts-DwrexFA4.js";import"./vendor-codemirror-DVE2_WBr.js";(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const o of document.querySelectorAll('link[rel="modulepreload"]'))i(o);new MutationObserver(o=>{for(const t of o)if(t.type==="childList")for(const l of t.addedNodes)l.tagName==="LINK"&&l.rel==="modulepreload"&&i(l)}).observe(document,{childList:!0,subtree:!0});function u(o){const t={};return o.integrity&&(t.integrity=o.integrity),o.referrerPolicy&&(t.referrerPolicy=o.referrerPolicy),o.crossOrigin==="use-credentials"?t.credentials="include":o.crossOrigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function i(o){if(o.ep)return;o.ep=!0;const t=u(o);fetch(o.href,t)}})();function ge(){return e(x,{styles:a=>h`
        body {
          background-color: var(--ac-global-color-grey-75);
          color: var(--ac-global-text-color-900);
          font-family: "Roboto";
          font-size: ${a.typography.sizes.medium.fontSize}px;
          margin: 0;
          overflow: hidden;
          #root,
          #root > div[data-overlay-container="true"],
          #root > div[data-overlay-container="true"] > .ac-theme {
            height: 100vh;
          }
        }

        /* Remove list styling */
        ul {
          display: block;
          list-style-type: none;
          margin-block-start: none;
          margin-block-end: 0;
          padding-inline-start: 0;
          margin-block-start: 0;
        }

        /* A reset style for buttons */
        .button--reset {
          background: none;
          border: none;
          padding: 0;
        }
        /* this css class is added to html via modernizr @see modernizr.js */
        .no-hiddenscroll {
          /* Works on Firefox */
          * {
            scrollbar-width: thin;
            scrollbar-color: var(--ac-global-color-grey-300)
              var(--ac-global-color-grey-400);
          }

          /* Works on Chrome, Edge, and Safari */
          *::-webkit-scrollbar {
            width: 14px;
          }

          *::-webkit-scrollbar-track {
            background: var(--ac-global-color-grey-100);
          }

          *::-webkit-scrollbar-thumb {
            background-color: var(--ac-global-color-grey-75);
            border-radius: 8px;
            border: 1px solid var(--ac-global-color-grey-300);
          }
        }

        :root {
          --px-blue-color: ${a.colors.arizeBlue};

          --px-flex-gap-sm: ${a.spacing.margin4}px;
          --px-flex-gap-sm: ${a.spacing.margin8}px;

          --px-section-background-color: ${a.colors.gray500};

          /* An item is a typically something in a list */
          --px-item-background-color: ${a.colors.gray800};
          --px-item-border-color: ${a.colors.gray600};

          --px-spacing-sm: ${a.spacing.padding4}px;
          --px-spacing-med: ${a.spacing.padding8}px;
          --px-spacing-lg: ${a.spacing.padding16}px;

          --px-border-radius-med: ${a.borderRadius.medium}px;

          --px-font-size-sm: ${a.typography.sizes.small.fontSize}px;
          --px-font-size-med: ${a.typography.sizes.medium.fontSize}px;
          --px-font-size-lg: ${a.typography.sizes.large.fontSize}px;

          --px-gradient-bar-height: 8px;

          --px-nav-collapsed-width: 45px;
          --px-nav-expanded-width: 200px;
        }

        .ac-theme--dark {
          --px-primary-color: #9efcfd;
          --px-primary-color--transparent: rgb(158, 252, 253, 0.2);
          --px-reference-color: #baa1f9;
          --px-reference-color--transparent: #baa1f982;
          --px-corpus-color: #92969c;
          --px-corpus-color--transparent: #92969c63;
        }
        .ac-theme--light {
          --px-primary-color: #00add0;
          --px-primary-color--transparent: rgba(0, 173, 208, 0.2);
          --px-reference-color: #4500d9;
          --px-reference-color--transparent: rgba(69, 0, 217, 0.2);
          --px-corpus-color: #92969c;
          --px-corpus-color--transparent: #92969c63;
        }
      `})}const ue=b(f(n(r,{path:"/",errorElement:e(k,{}),children:[e(r,{path:"/login",element:e(E,{})}),e(r,{path:"/reset-password",element:e($,{}),loader:j}),e(r,{path:"/reset-password-with-token",element:e(I,{})}),e(r,{path:"/forgot-password",element:e(S,{})}),e(r,{element:e(A,{}),loader:C,children:n(r,{element:e(F,{}),children:[e(r,{path:"/profile",handle:{crumb:()=>"profile"},element:e(T,{})}),e(r,{index:!0,loader:O}),n(r,{path:"/model",handle:{crumb:()=>"model"},element:e(D,{}),children:[e(r,{index:!0,element:e(d,{})}),e(r,{element:e(d,{}),children:e(r,{path:"dimensions",children:e(r,{path:":dimensionId",element:e(B,{}),loader:G})})}),e(r,{path:"embeddings",children:e(r,{path:":embeddingDimensionId",element:e(M,{}),loader:N,handle:{crumb:a=>a.embedding.name}})})]}),n(r,{path:"/projects",handle:{crumb:()=>"projects"},element:e(W,{}),children:[e(r,{index:!0,element:e(q,{})}),n(r,{path:":projectId",element:e(H,{}),loader:_,handle:{crumb:a=>a.project.name},children:[e(r,{index:!0,element:e(c,{})}),e(r,{element:e(c,{}),children:e(r,{path:"traces/:traceId",element:e(J,{})})})]})]}),n(r,{path:"/datasets",handle:{crumb:()=>"datasets"},children:[e(r,{index:!0,element:e(K,{})}),n(r,{path:":datasetId",loader:p,handle:{crumb:a=>a.dataset.name},children:[n(r,{element:e(Q,{}),loader:p,children:[e(r,{index:!0,element:e(m,{}),loader:g}),e(r,{path:"experiments",element:e(m,{}),loader:g}),e(r,{path:"examples",element:e(U,{}),loader:V,children:e(r,{path:":exampleId",element:e(X,{})})})]}),e(r,{path:"compare",handle:{crumb:()=>"compare"},loader:Y,element:e(Z,{})})]})]}),n(r,{path:"/playground",handle:{crumb:()=>"Playground"},children:[e(r,{index:!0,element:e(ee,{})}),e(r,{path:"spans/:spanId",element:e(re,{}),loader:ae,handle:{crumb:a=>a.span.__typename==="Span"?`span ${a.span.context.spanId}`:"span unknown"}})]}),e(r,{path:"/apis",element:e(oe,{}),handle:{crumb:()=>"APIs"}}),e(r,{path:"/settings",element:e(te,{}),handle:{crumb:()=>"Settings"}})]})})]})),{basename:window.Config.basename});function he(){return e(y,{router:ue})}function xe(){return e(ne,{children:e(ie,{children:e(be,{})})})}function be(){const{theme:a}=de();return e(z,{theme:a,children:e(P,{theme:L,children:n(w.RelayEnvironmentProvider,{environment:ce,children:[e(ge,{}),e(se,{children:e(pe,{children:e(le,{children:e(v.Suspense,{children:e(me,{children:e(he,{})})})})})})]})})})}const fe=document.getElementById("root"),ye=R.createRoot(fe);ye.render(e(xe,{}));
