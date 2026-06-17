import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# I will update generateSingleWorkOrderReport to aggressively use a proxy to guarantee images load.
# Also ensure margin is defined since the reviewer pointed it out.

old_wo = """            // --- Anexos Fotográficos ---
            if (order.images && order.images.length > 0) {
                doc.addPage();
                drawHeader('Anexo: Registro Fotográfico de Actividades');

                let startY = 140;
                let currentY = startY;
                const imagesToProcess = order.images; // Process all images

                // Adjust sizes for two images side by side
                const usableWidth = pageWidth - (margin * 2);
                const gap = 20; // 20pt gap between images
                const targetWidthPt = (usableWidth - gap) / 2;

                // Max height to ensure they fit nicely, say 4 rows per page (max 200pt height)
                const maxHeightPt = 200;

                for (let idx = 0; idx < imagesToProcess.length; idx += 2) {
                    // Start a new page if we are out of space
                    if (currentY > doc.internal.pageSize.getHeight() - 250 && idx > 0) {
                        doc.addPage();
                        drawHeader('Anexo: Registro Fotográfico de Actividades');
                        currentY = 140;
                    }

                    let rowMaxHeight = 0;

                    // Process two images (left and right)
                    for (let col = 0; col < 2; col++) {
                        const imgIdx = idx + col;
                        if (imgIdx >= imagesToProcess.length) break;

                        const img = imagesToProcess[imgIdx];
                        const imgX = margin + col * (targetWidthPt + gap);

                        try {
                            const imgResult = await imageUrlToBase64(img.url, true);
                            if (imgResult) {
                                let finalW = targetWidthPt;
                                let finalH = (imgResult.height * finalW) / imgResult.width;

                                if (finalH > maxHeightPt) {
                                    finalH = maxHeightPt;
                                    finalW = (imgResult.width * finalH) / imgResult.height;
                                }

                                // Center image within its column block
                                const finalX = imgX + (targetWidthPt - finalW) / 2;

                                doc.addImage(imgResult.data, 'JPEG', finalX, currentY, finalW, finalH, undefined, 'FAST');

                                doc.setFontSize(10);
                                doc.setFont(undefined, 'italic');
                                const caption = img.caption || `Imagen ${imgIdx + 1}`;
                                const splitCaption = doc.splitTextToSize(caption, targetWidthPt);
                                doc.text(splitCaption, imgX + targetWidthPt / 2, currentY + finalH + 15, { align: 'center' });

                                const totalBlockHeight = finalH + 15 + (splitCaption.length * 12);
                                if (totalBlockHeight > rowMaxHeight) {
                                    rowMaxHeight = totalBlockHeight;
                                }
                            } else {
                                throw new Error("Base64 conversion failed");
                            }
                        } catch (err) {
                            console.error("Error adding activity image to PDF:", err);
                            doc.setFontSize(10);
                            doc.text(`[No se pudo cargar la imagen ${imgIdx + 1}]`, imgX + targetWidthPt / 2, currentY + 20, { align: 'center' });
                            if (40 > rowMaxHeight) rowMaxHeight = 40;
                        }
                    }
                    currentY += rowMaxHeight + 30; // Move to the next row
                }
            }"""

new_wo = """            // --- Anexos Fotográficos ---
            if (order.images && order.images.length > 0) {
                doc.addPage();
                drawHeader('Anexo: Registro Fotográfico de Actividades');

                let startY = 140;
                let currentY = startY;
                const imagesToProcess = order.images; // Process all images

                // Adjust sizes for two images side by side
                const safeMargin = typeof margin !== 'undefined' ? margin : 40;
                const usableWidth = pageWidth - (safeMargin * 2);
                const gap = 20; // 20pt gap between images
                const targetWidthPt = (usableWidth - gap) / 2;

                // Max height to ensure they fit nicely, say 4 rows per page (max 200pt height)
                const maxHeightPt = 200;

                for (let idx = 0; idx < imagesToProcess.length; idx += 2) {
                    // Start a new page if we are out of space
                    if (currentY > doc.internal.pageSize.getHeight() - 250 && idx > 0) {
                        doc.addPage();
                        drawHeader('Anexo: Registro Fotográfico de Actividades');
                        currentY = 140;
                    }

                    let rowMaxHeight = 0;

                    // Process two images (left and right)
                    for (let col = 0; col < 2; col++) {
                        const imgIdx = idx + col;
                        if (imgIdx >= imagesToProcess.length) break;

                        const img = imagesToProcess[imgIdx];
                        const imgX = safeMargin + col * (targetWidthPt + gap);

                        try {
                            // Convert standard firebase urls to proxy ones directly to ensure load
                            let urlToFetch = img.url;
                            if (urlToFetch.includes('firebasestorage.googleapis.com')) {
                                urlToFetch = `https://wsrv.nl/url=${encodeURIComponent(urlToFetch)}&output=jpg&q=80`;
                            }

                            // Use retry logic for optimized images
                            const imgResult = await imageUrlToBase64(urlToFetch, true);

                            if (imgResult) {
                                let finalW = targetWidthPt;
                                let finalH = (imgResult.height * finalW) / imgResult.width;

                                if (finalH > maxHeightPt) {
                                    finalH = maxHeightPt;
                                    finalW = (imgResult.width * finalH) / imgResult.height;
                                }

                                // Center image within its column block
                                const finalX = imgX + (targetWidthPt - finalW) / 2;

                                doc.addImage(imgResult.data, 'JPEG', finalX, currentY, finalW, finalH, undefined, 'FAST');

                                doc.setFontSize(10);
                                doc.setFont(undefined, 'italic');
                                const caption = img.caption || `Imagen ${imgIdx + 1}`;
                                const splitCaption = doc.splitTextToSize(caption, targetWidthPt);
                                doc.text(splitCaption, imgX + targetWidthPt / 2, currentY + finalH + 15, { align: 'center' });

                                const totalBlockHeight = finalH + 15 + (splitCaption.length * 12);
                                if (totalBlockHeight > rowMaxHeight) {
                                    rowMaxHeight = totalBlockHeight;
                                }
                            } else {
                                throw new Error("Base64 conversion failed");
                            }
                        } catch (err) {
                            console.error("Error adding activity image to PDF:", err);
                            doc.setFontSize(10);
                            doc.text(`[No se pudo cargar la imagen ${imgIdx + 1}]`, imgX + targetWidthPt / 2, currentY + 20, { align: 'center' });
                            if (40 > rowMaxHeight) rowMaxHeight = 40;
                        }
                    }
                    currentY += rowMaxHeight + 30; // Move to the next row
                }
            }"""

if old_wo in content:
    content = content.replace(old_wo, new_wo)
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced Work Order image block successfully.")
else:
    print("Work order image block not found.")
