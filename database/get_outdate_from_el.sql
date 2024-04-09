SELECT el.*
FROM epimetric_latest el
LEFT JOIN (
    SELECT signal_key_id, geo_key_id, time_type, time_value, MAX(issue) AS latest_issue
    FROM epimetric_full
    GROUP BY signal_key_id, geo_key_id, time_type, time_value
) ef ON el.signal_key_id = ef.signal_key_id
    AND el.geo_key_id = ef.geo_key_id
    AND el.time_type = ef.time_type
    AND el.time_value = ef.time_value
WHERE ef.latest_issue IS NULL OR el.issue <> ef.latest_issue;