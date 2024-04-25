def emailGenerator(sampro_full: str, sampro_special: str, sampro_android: str, ms_licenses: str):
    return """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html dir="ltr" lang="en">
            <head>
                <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
                <style>
                @font-face {
                    font-family: 'Inter';
                    font-style: normal;
                    font-weight: 400;
                    mso-font-alt: 'sans-serif';
                    src: url(https://rsms.me/inter/font-files/Inter-Regular.woff2?v=3.19) format('woff2');
                }

                * {
                    font-family: 'Inter', sans-serif;
                }
                </style>
                <style>
                blockquote,
                h1,
                h2,
                h3,
                img,
                li,
                ol,
                p,
                ul {
                    margin-top: 0;
                    margin-bottom: 0
                }
                </style>
            </head>
            <body>
                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:600px;min-width:300px;width:100%;margin-left:auto;margin-right:auto;padding:0.5rem">
                <tbody>
                    <tr style="width:100%">
                    <td>
                        <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:37.5em;height:16px">
                        <tbody>
                            <tr style="width:100%">
                            <td></td>
                            </tr>
                        </tbody>
                        </table>
                        <h1 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:36px;line-height:40px;font-weight:800">
                        <strong>Daily License Usage Report</strong>
                        </h1>
                        <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:20px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                        <em>from </em>
                        <em>
                            <a href="mailto:it@wearetheone.com" rel="noopener noreferrer nofollow" style="color:rgb(17, 24, 39);text-decoration:underline;font-weight:500" target="_blank">it@wearetheone.com</a>
                        </em>
                        </p>
                        <h2 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:30px;line-height:36px;font-weight:700">Sampro</h2>
                        <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">

                """ + f"""
                        <tbody>
                            <tr style="width:100%">
                            <td>
                                <ul style="margin-top:0px;margin-bottom:20px;padding-left:26px;list-style-type:disc">
                                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
                                    <tbody>
                                    <tr style="width:100%">
                                        <td>
                                        <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <strong>Full User License</strong>
                                            </p>
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">{sampro_full}</p>
                                        </li>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
                                    <tbody>
                                    <tr style="width:100%">
                                        <td>
                                        <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <strong>Special User License</strong>
                                            </p>
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">{sampro_special}</p>
                                        </li>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
                                    <tbody>
                                    <tr style="width:100%">
                                        <td>
                                        <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
                                            <strong>TechAnywhere Licenses</strong>
                                            </p>
                                            <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">{sampro_android}</p>
                                        </li>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </ul>
                            </td>
                            </tr>
                        </tbody>
                        </table>
                        <h2 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:30px;line-height:36px;font-weight:700">Microsoft</h2>
                        <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
                        <tbody>
                            <tr style="width:100%">
                            <td>
                                <ul style="margin-top:0px;margin-bottom:20px;padding-left:26px;list-style-type:disc">
                                    {ms_licenses}
                                </ul>
                            </td>
                            </tr>
                        </tbody>
                        </table>
                    </td>
                    </tr>
                </tbody>
                </table>
            </body>
        </html>
    """
    # return """
    #     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    #     <html dir="ltr" lang="en">
    #     <head>
    #         <meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
    #         <style>
    #         @font-face {
    #             font-family: 'Inter';
    #             font-style: normal;
    #             font-weight: 400;
    #             mso-font-alt: 'sans-serif';
    #             src: url(https://rsms.me/inter/font-files/Inter-Regular.woff2?v=3.19) format('woff2');
    #         }

    #         * {
    #             font-family: 'Inter', sans-serif;
    #         }
    #         </style>
    #         <style>
    #         blockquote,
    #         h1,
    #         h2,
    #         h3,
    #         img,
    #         li,
    #         ol,
    #         p,
    #         ul {
    #             margin-top: 0;
    #             margin-bottom: 0
    #         }
    #         </style>
    #     </head>
    #     <body>
    #         <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:600px;min-width:300px;width:100%;margin-left:auto;margin-right:auto;padding:0.5rem">
    #         <tbody>
    #             <tr style="width:100%">
    #             <td>
    #                 <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:37.5em;height:64px">
    #                 <tbody>
    #                     <tr style="width:100%">
    #                     <td></td>
    #                     </tr>
    #                 </tbody>
    #                 </table>
    #                 <h2 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:30px;line-height:36px;font-weight:700">
    #                 <strong>Sampro Active License Daily Report</strong>
    #                 </h2>
    #                 <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:20px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                 <em>from: it@wearetheone.com</em>
    #                 </p>
    #                 <h3 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:24px;line-height:38px;font-weight:600">User Licenses</h3>
    #                 <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
    #                 <tbody>
    #                     <tr style="width:100%">
    #                     <td>
    #                         <ul style="margin-top:0px;margin-bottom:20px;padding-left:26px;list-style-type:disc">
    #                         <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
    #                             <tbody>
    #                             <tr style="width:100%">
    #                                 <td>
    # """ + f"""
    #                                 <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <strong>Full User License:</strong><p>  {sampro_full}</p>
    #                                     </p>
    #                                 </li>
    #                                 </td>
    #                             </tr>
    #                             </tbody>
    #                         </table>
    #                         <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
    #                             <tbody>
    #                             <tr style="width:100%">
    #                                 <td>
    #                                 <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <strong>Special User License:</strong><p>  {sampro_special}</p>
    #                                     </p>
    #                                 </li>
    #                                 </td>
    #                             </tr>
    #                             </tbody>
    #                         </table>
    #                         </ul>
    #                     </td>
    #                     </tr>
    #                 </tbody>
    #                 </table>
    #                 <h3 style="text-align:left;color:rgb(17, 24, 39);margin-bottom:12px;margin-top:0px;font-size:24px;line-height:38px;font-weight:600">Technician Licneses</h3>
    #                 <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
    #                 <tbody>
    #                     <tr style="width:100%">
    #                     <td>
    #                         <ul style="margin-top:0px;margin-bottom:20px;padding-left:26px;list-style-type:disc">
    #                         <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="max-width:100%">
    #                             <tbody>
    #                             <tr style="width:100%">
    #                                 <td>
    #                                 <li style="margin-bottom:8px;padding-left:6px;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <p style="font-size:15px;line-height:24px;margin:16px 0;text-align:left;margin-bottom:0px;margin-top:0px;color:rgb(55, 65, 81);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale">
    #                                     <strong>Android Technician Licenses:</strong><p>  {sampro_android}</p>
    #                                     </p>
    #                                 </li>
    #                                 </td>
    #                             </tr>
    #                             </tbody>
    #                         </table>
    #                         </ul>
    #                     </td>
    #                     </tr>
    #                 </tbody>
    #                 </table>
    #             </td>
    #             </tr>
    #         </tbody>
    #         </table>
    #     </body>
    #     </html>
    # """